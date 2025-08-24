# Generated from toniParser.g4 by ANTLR 4.13.2
import copy
import sys

from antlr4 import *

from .toniLexer import toniLexer
from .toniParser import toniParser

import string

from lib import toni_classes,toni_utils

# This class defines a complete generic visitor for a parse tree produced by toniParser.

class toniParserVisitor(ParseTreeVisitor):

    def compile(self, regex: str):
        # Set the state_counter to 0
        # For each compiled regex, the state counting
        # should start at 0
        #
        # This is used to know how many states are in
        # a regex
        toni_classes.state_counter = 0

        # Likewise, restart the dictionary of states,
        # where all states are stored and can easily
        # be accessed via their name (qX)
        toni_classes.state_dictionary = {}

        lexer = toniLexer(InputStream(regex))
        stream = CommonTokenStream(lexer)
        parser = toniParser(stream)

        # Visit the AST and apply Thompson's algorithm
        # to each node
        tree = parser.root()

        return self.visit(tree)

    def visitRoot(self, ctx):
        '''
        visitRoot

        In this node the start and ending states are created.
        Therefore, all dangling states left from the received
        partial NFAs will point to the final state.

        Additionally, if '^' or '$' are not present, a STAR_STATE
        is also added, to allow for input before or after the beginning
        of the regex.
        '''

        hasHat = ctx.HAT()
        hasDollar = ctx.DOLLAR()
        final_nfa = self.visit(ctx.regExp())

        if hasHat and hasDollar:
            start = toni_classes.State(-1,[final_nfa.start],False,True)
            end = toni_classes.State(-1,[],True)
            toni_utils.fix_dangling(final_nfa,end)
            return start
        elif not hasHat and not hasDollar:
            start = toni_classes.State(-1,[final_nfa.start],False,True)
            end = toni_classes.State(-1,[],True)
            toni_utils.fix_dangling(final_nfa,end)
            e_star_start = toni_classes.Star_State([start],False)
            e_star_end = toni_classes.Star_State([end],False)
            start.output_states.append(e_star_start)
            end.output_states.append(e_star_end)
            return start
        elif hasHat and not hasDollar:
            start = toni_classes.State(-1,[final_nfa.start],False,True)
            end = toni_classes.State(-1,[],True)
            toni_utils.fix_dangling(final_nfa,end)
            e_star_end = toni_classes.Star_State([end],False)
            end.output_states.append(e_star_end)
            return start
        elif not hasHat and hasDollar:
            start = toni_classes.State(-1,[final_nfa.start],False,True)
            end = toni_classes.State(-1,[],True)
            toni_utils.fix_dangling(final_nfa,end)
            e_star_start = toni_classes.Star_State([start],False)
            start.output_states.append(e_star_start)
            return start
    
    def visitRegExp(self, ctx):
        '''
        visitRegExp

        Node for branch expressions
        '''

        # If there is no branch, just return the child's partial NFA
        if len(ctx.branch()) == 1:
            return self.visit(ctx.branch()[0])
        
        # Otherwise, 
        #   a) obtain all partial NFAs from the children
        #   b) create a new state, which can have many alternative paths (|)
        #   c) have all children NFAs starting state as a possible
        #      output state. Their dangling states will also be this
        #      new NFA's dangling states
        branch_list_states = []
        branch_list_dangling = []
        for branch in ctx.branch():
            current_branch = self.visit(branch)
            branch_list_states.append(current_branch.start)
            branch_list_dangling.extend(current_branch.dangling_states)
        s = toni_classes.State(-1, branch_list_states, False)
        f = toni_classes.Partial_NFA(s, branch_list_dangling)

        return f
    
    def visitBranch(self, ctx):
        '''
        visitBranch

        Visit node for a piece. These pieces are single elements in a branch,
        which can be chained to make one of the paths in the branch
        '''

        # If there is only one piece, return the child's partial NFA
        if len(ctx.piece()) == 1:
            return self.visit(ctx.piece()[0])
        first_piece = self.visit(ctx.piece()[0])

        # Otherwise chain the pieces, i.e. point the output state of partial NFA i
        # to the starting state of partial NFA i+1
        for piece in ctx.piece()[1:]:
            next_piece = self.visit(piece)
            toni_utils.fix_dangling(first_piece,next_piece.start)
            first_piece = toni_classes.Partial_NFA(first_piece.start,next_piece.dangling_states)

        return first_piece

    def visitPiece(self, ctx):
        '''
        Visit node for piece, which is an expression which can
        be quantified
        '''

        # Visit the element which is going to be quantified
        to_be_quantified = self.visit(ctx.atom())

        # If there is no quantifier, return the element
        if not ctx.quantifier():
            return to_be_quantified
        # If '*', the new state can process the expression as
        # many times as it wants, or none
        elif ctx.quantifier().STAR():
            s = toni_classes.State(-1, [to_be_quantified.start], False)
            toni_utils.fix_dangling(to_be_quantified, s)
            f = toni_classes.Partial_NFA(s, [s])
            return f
        # If '?', new state can either process the expression
        # once or none
        elif ctx.quantifier().QUESTION():
            s = toni_classes.State(-1, [to_be_quantified.start], False)

            tmp_dangling_states = [s]
            tmp_dangling_states.extend(to_be_quantified.dangling_states)

            f = toni_classes.Partial_NFA(s, tmp_dangling_states)
            return f
        # If '+', new state has to process the expression at least
        # once
        elif ctx.quantifier().PLUS():
            s = toni_classes.State(-1, [to_be_quantified.start], False)
            toni_utils.fix_dangling(to_be_quantified, s)

            f = toni_classes.Partial_NFA(to_be_quantified.start, [s])
            return f
        else:
            # Otherwise, it's a quantifier
            # Therefore, get the type of quantifier, max and min
            quantity = self.visit(ctx.quantifier().quantity())
            quantity_min = quantity["min"]
            quantity_max = quantity["max"]
            base = None

            # Range - expression can happen between min and max
            if quantity["type"] == "range":
                if quantity_min == 0:
                    print("If MIN 0 in RANGE, use MAX instead.")
                    sys.exit(1)
                elif quantity_min > quantity_max:
                    print("MIN cannot be greater than MAX in RANGE")
                    sys.exit(1)
                elif quantity_min == quantity_max:
                    print("If MIN and MAX are equal use EXACT")

                base = copy.deepcopy(to_be_quantified)
                missing_dangling = []

                for _ in range(quantity_min-1):
                    e = copy.deepcopy(to_be_quantified)
                    toni_utils.fix_dangling(base, e.start)
                    base = toni_classes.Partial_NFA(base.start, e.dangling_states)
                for _ in range(quantity_max - quantity_min):
                    e = copy.deepcopy(to_be_quantified)
                    s = toni_classes.State(-1, [e.start], False)
                    missing_dangling.append(s)
                    toni_utils.fix_dangling(base, s)
                    base = toni_classes.Partial_NFA(base.start, e.dangling_states)

                # Add the one base dangling we have from the last transition and the missing dangling from the 
                # state after the min iteration and the dangling in between that state and the last transition
                base.dangling_states.extend(missing_dangling)
                base = toni_classes.Partial_NFA(base.start, base.dangling_states)
            # Min - expression has to be processed at least min times
            elif quantity["type"] == "min":

                if quantity_min == 0:
                    print("If MIN 0 in MIN, use * instead.")
                    sys.exit(1)
                elif quantity_min == 1:
                    print("If MIN 1 in MIN, use + instead.")
                    sys.exit(1)

                base = copy.deepcopy(to_be_quantified)

                for _ in range(quantity_min-1):
                    e = copy.deepcopy(to_be_quantified)
                    toni_utils.fix_dangling(base, e.start)
                    base = toni_classes.Partial_NFA(base.start, e.dangling_states)
                e = copy.deepcopy(to_be_quantified)
                s = toni_classes.State(-1, [e.start], False)
                toni_utils.fix_dangling(e, s)
                toni_utils.fix_dangling(base, s)
                base = toni_classes.Partial_NFA(base.start, [s])
            # Max - expression has to be processed at most max times
            elif quantity["type"] == "max":

                e = copy.deepcopy(to_be_quantified)
                s = toni_classes.State(-1, [e.start], False)
                base = toni_classes.Partial_NFA(s, e.dangling_states)
                missing_dangling = [s]

                for _ in range(quantity_max-1):
                    e = copy.deepcopy(to_be_quantified)
                    s = toni_classes.State(-1, [e.start], False)
                    missing_dangling.append(s)
                    toni_utils.fix_dangling(base, s)
                    base = toni_classes.Partial_NFA(base.start, e.dangling_states)

                base.dangling_states.extend(missing_dangling)
                base = toni_classes.Partial_NFA(base.start, base.dangling_states)
            # Eact - expression has to be processed exactly exact times
            elif quantity["type"] == "exact":

                if quantity_min == 0:
                    print("An EXACT with 0 is useless. Remove it.")
                    sys.exit(1)

                base = copy.deepcopy(to_be_quantified)

                for _ in range(quantity_min-1):
                    e = copy.deepcopy(to_be_quantified)
                    toni_utils.fix_dangling(base, e.start)
                    base = toni_utils.Partial_NFA(base.start, e.dangling_states)

            return base

    def visitQuantity(self, ctx):
        '''
        visitQuantity

        Visit node for quantity, simply check what is the type
        of the node and obtain the parameters accordingly
        '''
        quantity = {"type": "", "min": 0, "max": 0}

        if ctx.quantRange():
            quantity["type"] = "range"
            quantity["min"] = int(ctx.quantRange().QuantExact()[0].getText())
            quantity["max"] = int(ctx.quantRange().QuantExact()[1].getText())
        elif ctx.quantMin():
            quantity["type"] = "min"
            quantity["min"] = int(ctx.quantMin().QuantExact().getText())
        elif ctx.quantMax():
            quantity["type"] = "max"
            quantity["max"] = int(ctx.quantMax().QuantExact().getText())
        elif ctx.QuantExact():
            quantity["type"] = "exact"
            quantity["min"] = int(ctx.QuantExact().getText())

        return quantity

    def visitAtom(self, ctx):
        '''
        visitAtom

        Visit an atomi expression. This can be either a char class,
        such as a set of characters, a single character or a
        parenthesized expression
        '''

        f = None
        if ctx.charClass():
            # If it's a char class, obtain what characters are accepted
            allowed_states = self.visit(ctx.charClass())
            s = toni_classes.Char_Class_State(allowed_states, [], False)
            f = toni_classes.Partial_NFA(s, [s])
        elif ctx.Char():
            # If it's just a char, obtain it directly from the expression
            character_code = ord(ctx.Char().getText())
            s = toni_classes.State(character_code, [], False)
            f = toni_classes.Partial_NFA(s, [s])
        else:
            # Otherwise, it's a parenthesized expression, return it immediately
            f = self.visit(ctx.regExp())

        return f
    
    def visitCharClass(self, ctx):
        '''
        visitCharClass

        Visit the char class node, above all it should
        determine what are the accepted characters
        '''

        # A '.' should accept all characters except '\n',
        # with ASCII code 10
        if ctx.WildcardEsc():
            chars = [x for x in range(10)]
            chars.extend([y for y in range(11,256)])
            return chars
        # Otherwise, visit the child directly
        elif ctx.charClassEsc():
            return self.visit(ctx.charClassEsc())
        elif ctx.charClassExpr():
            return self.visit(ctx.charClassExpr())

    def visitCharClassEsc(self, ctx):
        '''
        visitCharClassEsc

        Visit escaped char classes, which are just escaped
        characters to simbolize certain elements

        The meaning attributed to each symbol can be found here:
        https://www.dataquest.io/cheat-sheet/regular-expressions-cheat-sheet/
        '''

        text = ctx.getText()
        if text == "\\n":
            return [ord("\n")]
        elif text == "\\r":
            return [ord("\r")]
        elif text == "\\t":
            return [ord("\t")]
        elif text == "\w":
            chars = [ord(x) for x in (string.ascii_letters + string.digits + "_")]
            return chars
        elif text == "\W":
            chars = [ord(x) for x in (string.ascii_letters + string.digits + "_")]
            return [x for x in range(0,256) if x not in chars]
        elif text == "\d":
            return [ord(x) for x in string.digits]
        elif text == "\D":
            digits = [ord(x) for x in string.digits]
            return [x for x in range(0,256) if x not in digits]
        elif text == "\s":
            return [ord(x) for x in ("\t","\n","\r"," ")]
        elif text == "\S":
            whitespaces = [ord(x) for x in ("\t","\n","\r"," ")]
            return [x for x in range(0,256) if x not in whitespaces]
        else:
            return [ord(text[1])]

    def visitCharClassExpr(self, ctx):
        '''
        visitCharClassExpr

        This is the first step, where we just decide if
        it's a positive char group, so all characters inside
        are allowed, or a negative char group, so all characters
        inside are forbidden
        '''

        exclusive = False # Base case therefore is PosCharGroup()
        if ctx.NegCharGroup():
            exclusive = True

        allowed_chars = self.visit(ctx.charGroup())
        if not exclusive:
            return allowed_chars
        else:
            # If exclusive, remove all the mentioned symbols
            return [x for x in range(0,256) if x not in allowed_chars]

    def visitCharGroup(self, ctx):
        '''
        visitCharGroup

        Decide if there is a range or only the symbol '-'
        '''

        allowed_chars = []
        if ctx.posCharGroup():
            allowed_chars = self.visit(ctx.posCharGroup())
            if ctx.DASH():
                allowed_chars.append(ord("-"))
        else:
            return [ord("-")]

        return allowed_chars

    def visitPosCharGroup(self, ctx):
        '''
        visitPosCharGroup

        Decide if we have escaped characters inside the group of ranges.
        Since we can have multiple of both types, we need to do this for all
        children of the node
        '''

        characters_to_allow = []
        index = 0
        children = ctx.getChildCount()
        # If the first character is '-', add it to allowed characters
        if ctx.getChild(index) == "-":
            characters_to_allow.append(ord("-"))
            index += 1
        
        # Process char range
        if isinstance(ctx.getChild(index), toniParser.CharRangeContext):
            characters_to_allow.extend(self.visit(ctx.getChild(index)))
            index += 1
        # Process escaped character
        elif isinstance(ctx.getChild(index), toniParser.CharClassEscContext):
            characters_to_allow.extend(self.visit(ctx.getChild(index)))
            index += 1
        
        # Repeat for all children
        while index < children:
            if ctx.getChild(index) == "-" and not ord("-") in characters_to_allow:
                characters_to_allow.append(ord("-"))
            elif isinstance(ctx.getChild(index), toniParser.CharRangeContext):
                characters_to_allow.extend(self.visit(ctx.getChild(index)))
            elif isinstance(ctx.getChild(index), toniParser.CharClassEscContext):
                characters_to_allow.extend(self.visit(ctx.getChild(index)))
            index += 1

        return characters_to_allow

    def visitCharRange(self, ctx):
        '''
        visitCharRange

        To determine the range, we calculate the ASCII code of the
        edges and include all characters in the middle
        '''

        if ctx.seRange():
            start = self.visit(ctx.seRange().charOrEsc()[0])
            end = self.visit(ctx.seRange().charOrEsc()[1])
            if start > end:
                print("In a range the end must be bigger than the start")
                sys.exit(1)
            return [x for x in range(start,end+1)]
        else:
            return [ord(ctx.XmlChar().getText())]

    def visitCharOrEsc(self, ctx):
        '''
        visitCharOrEsc

        Determine if it's a character or an escaped character
        '''

        text = ctx.getText()
        if ctx.SingleCharEsc():
            if text == "\\n":
                return ord("\n")
            elif text == "\\r":
                return ord("\r")
            elif text == "\\t":
                return ord("\t")
            else:
                return ord(text[1])
        else:
            return ord(text)

