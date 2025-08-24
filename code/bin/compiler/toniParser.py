# Generated from toniParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,3,0,44,8,0,1,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,5,1,55,
        8,1,10,1,12,1,58,9,1,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,3,1,3,3,3,
        68,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,3,
        5,83,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,101,8,9,1,10,1,10,1,10,3,10,106,8,10,1,11,1,11,1,11,
        1,11,1,12,1,12,3,12,114,8,12,1,12,3,12,117,8,12,1,13,3,13,120,8,
        13,1,13,1,13,3,13,124,8,13,1,13,3,13,127,8,13,1,13,1,13,3,13,131,
        8,13,5,13,133,8,13,10,13,12,13,136,9,13,1,14,1,14,3,14,140,8,14,
        1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,0,6,1,0,16,17,2,0,12,12,39,39,2,0,
        12,13,31,32,2,0,14,14,33,33,2,0,15,15,34,34,2,0,22,22,30,30,161,
        0,43,1,0,0,0,2,51,1,0,0,0,4,62,1,0,0,0,6,65,1,0,0,0,8,76,1,0,0,0,
        10,82,1,0,0,0,12,84,1,0,0,0,14,88,1,0,0,0,16,91,1,0,0,0,18,100,1,
        0,0,0,20,105,1,0,0,0,22,107,1,0,0,0,24,116,1,0,0,0,26,119,1,0,0,
        0,28,139,1,0,0,0,30,141,1,0,0,0,32,145,1,0,0,0,34,147,1,0,0,0,36,
        149,1,0,0,0,38,153,1,0,0,0,40,157,1,0,0,0,42,44,5,8,0,0,43,42,1,
        0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,47,3,2,1,0,46,48,5,9,0,0,47,
        46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,
        0,51,56,3,4,2,0,52,53,5,3,0,0,53,55,3,4,2,0,54,52,1,0,0,0,55,58,
        1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,3,1,0,0,0,58,56,1,0,0,0,59,
        61,3,6,3,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,
        0,63,5,1,0,0,0,64,62,1,0,0,0,65,67,3,18,9,0,66,68,3,8,4,0,67,66,
        1,0,0,0,67,68,1,0,0,0,68,7,1,0,0,0,69,77,5,5,0,0,70,77,5,6,0,0,71,
        77,5,4,0,0,72,73,5,11,0,0,73,74,3,10,5,0,74,75,5,18,0,0,75,77,1,
        0,0,0,76,69,1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,77,
        9,1,0,0,0,78,83,3,12,6,0,79,83,3,14,7,0,80,83,3,16,8,0,81,83,5,19,
        0,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,11,
        1,0,0,0,84,85,5,19,0,0,85,86,5,20,0,0,86,87,5,19,0,0,87,13,1,0,0,
        0,88,89,5,19,0,0,89,90,5,20,0,0,90,15,1,0,0,0,91,92,5,20,0,0,92,
        93,5,19,0,0,93,17,1,0,0,0,94,101,5,10,0,0,95,101,3,20,10,0,96,97,
        5,1,0,0,97,98,3,2,1,0,98,99,5,2,0,0,99,101,1,0,0,0,100,94,1,0,0,
        0,100,95,1,0,0,0,100,96,1,0,0,0,101,19,1,0,0,0,102,106,3,34,17,0,
        103,106,3,22,11,0,104,106,5,7,0,0,105,102,1,0,0,0,105,103,1,0,0,
        0,105,104,1,0,0,0,106,21,1,0,0,0,107,108,7,0,0,0,108,109,3,24,12,
        0,109,110,5,37,0,0,110,23,1,0,0,0,111,113,3,26,13,0,112,114,5,38,
        0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,117,1,0,0,0,115,117,5,38,
        0,0,116,111,1,0,0,0,116,115,1,0,0,0,117,25,1,0,0,0,118,120,5,38,
        0,0,119,118,1,0,0,0,119,120,1,0,0,0,120,123,1,0,0,0,121,124,3,28,
        14,0,122,124,3,34,17,0,123,121,1,0,0,0,123,122,1,0,0,0,124,134,1,
        0,0,0,125,127,5,38,0,0,126,125,1,0,0,0,126,127,1,0,0,0,127,130,1,
        0,0,0,128,131,3,28,14,0,129,131,3,34,17,0,130,128,1,0,0,0,130,129,
        1,0,0,0,131,133,1,0,0,0,132,126,1,0,0,0,133,136,1,0,0,0,134,132,
        1,0,0,0,134,135,1,0,0,0,135,27,1,0,0,0,136,134,1,0,0,0,137,140,3,
        30,15,0,138,140,5,39,0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,29,
        1,0,0,0,141,142,3,32,16,0,142,143,5,38,0,0,143,144,3,32,16,0,144,
        31,1,0,0,0,145,146,7,1,0,0,146,33,1,0,0,0,147,148,7,2,0,0,148,35,
        1,0,0,0,149,150,7,3,0,0,150,151,3,40,20,0,151,152,5,21,0,0,152,37,
        1,0,0,0,153,154,7,4,0,0,154,155,3,40,20,0,155,156,5,21,0,0,156,39,
        1,0,0,0,157,158,7,5,0,0,158,41,1,0,0,0,17,43,47,56,62,67,76,82,100,
        105,113,116,119,123,126,130,134,139
    ]

class toniParser ( Parser ):

    grammarFileName = "toniParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'|'", "'+'", "'?'", "'*'", 
                     "'.'", "'^'", "'$'", "<INVALID>", "'{'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "']'", "'-'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "PIPE", "PLUS", "QUESTION", 
                      "STAR", "WildcardEsc", "HAT", "DOLLAR", "Char", "StartQuantity", 
                      "SingleCharEsc", "MultiCharEsc", "CatEsc", "ComplEsc", 
                      "NegCharGroup", "PosCharGroup", "EndQuantity", "QuantExact", 
                      "COMMA", "EndCategory", "IsCategory", "Letters", "Marks", 
                      "Numbers", "Punctuation", "Separators", "Symbols", 
                      "Others", "IsBlock", "NestedSingleCharEsc", "NestedMultiCharEsc", 
                      "NestedCatEsc", "NestedComplEsc", "NestedNegCharGroup", 
                      "NestedPosCharGroup", "EndCharGroup", "DASH", "XmlChar" ]

    RULE_root = 0
    RULE_regExp = 1
    RULE_branch = 2
    RULE_piece = 3
    RULE_quantifier = 4
    RULE_quantity = 5
    RULE_quantRange = 6
    RULE_quantMin = 7
    RULE_quantMax = 8
    RULE_atom = 9
    RULE_charClass = 10
    RULE_charClassExpr = 11
    RULE_charGroup = 12
    RULE_posCharGroup = 13
    RULE_charRange = 14
    RULE_seRange = 15
    RULE_charOrEsc = 16
    RULE_charClassEsc = 17
    RULE_catEsc = 18
    RULE_complEsc = 19
    RULE_charProp = 20

    ruleNames =  [ "root", "regExp", "branch", "piece", "quantifier", "quantity", 
                   "quantRange", "quantMin", "quantMax", "atom", "charClass", 
                   "charClassExpr", "charGroup", "posCharGroup", "charRange", 
                   "seRange", "charOrEsc", "charClassEsc", "catEsc", "complEsc", 
                   "charProp" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PIPE=3
    PLUS=4
    QUESTION=5
    STAR=6
    WildcardEsc=7
    HAT=8
    DOLLAR=9
    Char=10
    StartQuantity=11
    SingleCharEsc=12
    MultiCharEsc=13
    CatEsc=14
    ComplEsc=15
    NegCharGroup=16
    PosCharGroup=17
    EndQuantity=18
    QuantExact=19
    COMMA=20
    EndCategory=21
    IsCategory=22
    Letters=23
    Marks=24
    Numbers=25
    Punctuation=26
    Separators=27
    Symbols=28
    Others=29
    IsBlock=30
    NestedSingleCharEsc=31
    NestedMultiCharEsc=32
    NestedCatEsc=33
    NestedComplEsc=34
    NestedNegCharGroup=35
    NestedPosCharGroup=36
    EndCharGroup=37
    DASH=38
    XmlChar=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regExp(self):
            return self.getTypedRuleContext(toniParser.RegExpContext,0)


        def EOF(self):
            return self.getToken(toniParser.EOF, 0)

        def HAT(self):
            return self.getToken(toniParser.HAT, 0)

        def DOLLAR(self):
            return self.getToken(toniParser.DOLLAR, 0)

        def getRuleIndex(self):
            return toniParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = toniParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 42
                self.match(toniParser.HAT)


            self.state = 45
            self.regExp()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 46
                self.match(toniParser.DOLLAR)


            self.state = 49
            self.match(toniParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def branch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toniParser.BranchContext)
            else:
                return self.getTypedRuleContext(toniParser.BranchContext,i)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(toniParser.PIPE)
            else:
                return self.getToken(toniParser.PIPE, i)

        def getRuleIndex(self):
            return toniParser.RULE_regExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegExp" ):
                return visitor.visitRegExp(self)
            else:
                return visitor.visitChildren(self)




    def regExp(self):

        localctx = toniParser.RegExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_regExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.branch()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 52
                self.match(toniParser.PIPE)
                self.state = 53
                self.branch()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def piece(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toniParser.PieceContext)
            else:
                return self.getTypedRuleContext(toniParser.PieceContext,i)


        def getRuleIndex(self):
            return toniParser.RULE_branch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch" ):
                return visitor.visitBranch(self)
            else:
                return visitor.visitChildren(self)




    def branch(self):

        localctx = toniParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_branch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6442660994) != 0):
                self.state = 59
                self.piece()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PieceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(toniParser.AtomContext,0)


        def quantifier(self):
            return self.getTypedRuleContext(toniParser.QuantifierContext,0)


        def getRuleIndex(self):
            return toniParser.RULE_piece

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiece" ):
                return visitor.visitPiece(self)
            else:
                return visitor.visitChildren(self)




    def piece(self):

        localctx = toniParser.PieceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_piece)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.atom()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2160) != 0):
                self.state = 66
                self.quantifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(toniParser.QUESTION, 0)

        def STAR(self):
            return self.getToken(toniParser.STAR, 0)

        def PLUS(self):
            return self.getToken(toniParser.PLUS, 0)

        def StartQuantity(self):
            return self.getToken(toniParser.StartQuantity, 0)

        def quantity(self):
            return self.getTypedRuleContext(toniParser.QuantityContext,0)


        def EndQuantity(self):
            return self.getToken(toniParser.EndQuantity, 0)

        def getRuleIndex(self):
            return toniParser.RULE_quantifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantifier" ):
                return visitor.visitQuantifier(self)
            else:
                return visitor.visitChildren(self)




    def quantifier(self):

        localctx = toniParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quantifier)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(toniParser.QUESTION)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(toniParser.STAR)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(toniParser.PLUS)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(toniParser.StartQuantity)
                self.state = 73
                self.quantity()
                self.state = 74
                self.match(toniParser.EndQuantity)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantRange(self):
            return self.getTypedRuleContext(toniParser.QuantRangeContext,0)


        def quantMin(self):
            return self.getTypedRuleContext(toniParser.QuantMinContext,0)


        def quantMax(self):
            return self.getTypedRuleContext(toniParser.QuantMaxContext,0)


        def QuantExact(self):
            return self.getToken(toniParser.QuantExact, 0)

        def getRuleIndex(self):
            return toniParser.RULE_quantity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity" ):
                return visitor.visitQuantity(self)
            else:
                return visitor.visitChildren(self)




    def quantity(self):

        localctx = toniParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quantity)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.quantRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.quantMin()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.quantMax()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(toniParser.QuantExact)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QuantExact(self, i:int=None):
            if i is None:
                return self.getTokens(toniParser.QuantExact)
            else:
                return self.getToken(toniParser.QuantExact, i)

        def COMMA(self):
            return self.getToken(toniParser.COMMA, 0)

        def getRuleIndex(self):
            return toniParser.RULE_quantRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantRange" ):
                return visitor.visitQuantRange(self)
            else:
                return visitor.visitChildren(self)




    def quantRange(self):

        localctx = toniParser.QuantRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quantRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(toniParser.QuantExact)
            self.state = 85
            self.match(toniParser.COMMA)
            self.state = 86
            self.match(toniParser.QuantExact)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantMinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QuantExact(self):
            return self.getToken(toniParser.QuantExact, 0)

        def COMMA(self):
            return self.getToken(toniParser.COMMA, 0)

        def getRuleIndex(self):
            return toniParser.RULE_quantMin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantMin" ):
                return visitor.visitQuantMin(self)
            else:
                return visitor.visitChildren(self)




    def quantMin(self):

        localctx = toniParser.QuantMinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quantMin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(toniParser.QuantExact)
            self.state = 89
            self.match(toniParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantMaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(toniParser.COMMA, 0)

        def QuantExact(self):
            return self.getToken(toniParser.QuantExact, 0)

        def getRuleIndex(self):
            return toniParser.RULE_quantMax

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantMax" ):
                return visitor.visitQuantMax(self)
            else:
                return visitor.visitChildren(self)




    def quantMax(self):

        localctx = toniParser.QuantMaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_quantMax)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(toniParser.COMMA)
            self.state = 92
            self.match(toniParser.QuantExact)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Char(self):
            return self.getToken(toniParser.Char, 0)

        def charClass(self):
            return self.getTypedRuleContext(toniParser.CharClassContext,0)


        def LPAREN(self):
            return self.getToken(toniParser.LPAREN, 0)

        def regExp(self):
            return self.getTypedRuleContext(toniParser.RegExpContext,0)


        def RPAREN(self):
            return self.getToken(toniParser.RPAREN, 0)

        def getRuleIndex(self):
            return toniParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = toniParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(toniParser.Char)
                pass
            elif token in [7, 12, 13, 16, 17, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.charClass()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(toniParser.LPAREN)
                self.state = 97
                self.regExp()
                self.state = 98
                self.match(toniParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charClassEsc(self):
            return self.getTypedRuleContext(toniParser.CharClassEscContext,0)


        def charClassExpr(self):
            return self.getTypedRuleContext(toniParser.CharClassExprContext,0)


        def WildcardEsc(self):
            return self.getToken(toniParser.WildcardEsc, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charClass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClass" ):
                return visitor.visitCharClass(self)
            else:
                return visitor.visitChildren(self)




    def charClass(self):

        localctx = toniParser.CharClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_charClass)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.charClassEsc()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.charClassExpr()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(toniParser.WildcardEsc)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charGroup(self):
            return self.getTypedRuleContext(toniParser.CharGroupContext,0)


        def EndCharGroup(self):
            return self.getToken(toniParser.EndCharGroup, 0)

        def NegCharGroup(self):
            return self.getToken(toniParser.NegCharGroup, 0)

        def PosCharGroup(self):
            return self.getToken(toniParser.PosCharGroup, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charClassExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClassExpr" ):
                return visitor.visitCharClassExpr(self)
            else:
                return visitor.visitChildren(self)




    def charClassExpr(self):

        localctx = toniParser.CharClassExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_charClassExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 108
            self.charGroup()
            self.state = 109
            self.match(toniParser.EndCharGroup)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def posCharGroup(self):
            return self.getTypedRuleContext(toniParser.PosCharGroupContext,0)


        def DASH(self):
            return self.getToken(toniParser.DASH, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charGroup

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharGroup" ):
                return visitor.visitCharGroup(self)
            else:
                return visitor.visitChildren(self)




    def charGroup(self):

        localctx = toniParser.CharGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_charGroup)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.posCharGroup()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 112
                    self.match(toniParser.DASH)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(toniParser.DASH)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PosCharGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charRange(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toniParser.CharRangeContext)
            else:
                return self.getTypedRuleContext(toniParser.CharRangeContext,i)


        def charClassEsc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toniParser.CharClassEscContext)
            else:
                return self.getTypedRuleContext(toniParser.CharClassEscContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(toniParser.DASH)
            else:
                return self.getToken(toniParser.DASH, i)

        def getRuleIndex(self):
            return toniParser.RULE_posCharGroup

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPosCharGroup" ):
                return visitor.visitPosCharGroup(self)
            else:
                return visitor.visitChildren(self)




    def posCharGroup(self):

        localctx = toniParser.PosCharGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_posCharGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 118
                self.match(toniParser.DASH)


            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 121
                self.charRange()
                pass

            elif la_ == 2:
                self.state = 122
                self.charClassEsc()
                pass


            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==38:
                        self.state = 125
                        self.match(toniParser.DASH)


                    self.state = 130
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        self.state = 128
                        self.charRange()
                        pass

                    elif la_ == 2:
                        self.state = 129
                        self.charClassEsc()
                        pass

             
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seRange(self):
            return self.getTypedRuleContext(toniParser.SeRangeContext,0)


        def XmlChar(self):
            return self.getToken(toniParser.XmlChar, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharRange" ):
                return visitor.visitCharRange(self)
            else:
                return visitor.visitChildren(self)




    def charRange(self):

        localctx = toniParser.CharRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_charRange)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.seRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(toniParser.XmlChar)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charOrEsc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(toniParser.CharOrEscContext)
            else:
                return self.getTypedRuleContext(toniParser.CharOrEscContext,i)


        def DASH(self):
            return self.getToken(toniParser.DASH, 0)

        def getRuleIndex(self):
            return toniParser.RULE_seRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeRange" ):
                return visitor.visitSeRange(self)
            else:
                return visitor.visitChildren(self)




    def seRange(self):

        localctx = toniParser.SeRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_seRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.charOrEsc()
            self.state = 142
            self.match(toniParser.DASH)
            self.state = 143
            self.charOrEsc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharOrEscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XmlChar(self):
            return self.getToken(toniParser.XmlChar, 0)

        def SingleCharEsc(self):
            return self.getToken(toniParser.SingleCharEsc, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charOrEsc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharOrEsc" ):
                return visitor.visitCharOrEsc(self)
            else:
                return visitor.visitChildren(self)




    def charOrEsc(self):

        localctx = toniParser.CharOrEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_charOrEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==12 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharClassEscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SingleCharEsc(self):
            return self.getToken(toniParser.SingleCharEsc, 0)

        def NestedSingleCharEsc(self):
            return self.getToken(toniParser.NestedSingleCharEsc, 0)

        def MultiCharEsc(self):
            return self.getToken(toniParser.MultiCharEsc, 0)

        def NestedMultiCharEsc(self):
            return self.getToken(toniParser.NestedMultiCharEsc, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charClassEsc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharClassEsc" ):
                return visitor.visitCharClassEsc(self)
            else:
                return visitor.visitChildren(self)




    def charClassEsc(self):

        localctx = toniParser.CharClassEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_charClassEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6442463232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatEscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charProp(self):
            return self.getTypedRuleContext(toniParser.CharPropContext,0)


        def EndCategory(self):
            return self.getToken(toniParser.EndCategory, 0)

        def CatEsc(self):
            return self.getToken(toniParser.CatEsc, 0)

        def NestedCatEsc(self):
            return self.getToken(toniParser.NestedCatEsc, 0)

        def getRuleIndex(self):
            return toniParser.RULE_catEsc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatEsc" ):
                return visitor.visitCatEsc(self)
            else:
                return visitor.visitChildren(self)




    def catEsc(self):

        localctx = toniParser.CatEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_catEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not(_la==14 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 150
            self.charProp()
            self.state = 151
            self.match(toniParser.EndCategory)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplEscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def charProp(self):
            return self.getTypedRuleContext(toniParser.CharPropContext,0)


        def EndCategory(self):
            return self.getToken(toniParser.EndCategory, 0)

        def ComplEsc(self):
            return self.getToken(toniParser.ComplEsc, 0)

        def NestedComplEsc(self):
            return self.getToken(toniParser.NestedComplEsc, 0)

        def getRuleIndex(self):
            return toniParser.RULE_complEsc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplEsc" ):
                return visitor.visitComplEsc(self)
            else:
                return visitor.visitChildren(self)




    def complEsc(self):

        localctx = toniParser.ComplEscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_complEsc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not(_la==15 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 154
            self.charProp()
            self.state = 155
            self.match(toniParser.EndCategory)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IsCategory(self):
            return self.getToken(toniParser.IsCategory, 0)

        def IsBlock(self):
            return self.getToken(toniParser.IsBlock, 0)

        def getRuleIndex(self):
            return toniParser.RULE_charProp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharProp" ):
                return visitor.visitCharProp(self)
            else:
                return visitor.visitChildren(self)




    def charProp(self):

        localctx = toniParser.CharPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_charProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==22 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





