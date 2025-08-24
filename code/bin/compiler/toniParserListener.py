# Generated from toniParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .toniParser import toniParser
else:
    from toniParser import toniParser

# This class defines a complete listener for a parse tree produced by toniParser.
class toniParserListener(ParseTreeListener):

    # Enter a parse tree produced by toniParser#root.
    def enterRoot(self, ctx:toniParser.RootContext):
        pass

    # Exit a parse tree produced by toniParser#root.
    def exitRoot(self, ctx:toniParser.RootContext):
        pass


    # Enter a parse tree produced by toniParser#regExp.
    def enterRegExp(self, ctx:toniParser.RegExpContext):
        pass

    # Exit a parse tree produced by toniParser#regExp.
    def exitRegExp(self, ctx:toniParser.RegExpContext):
        pass


    # Enter a parse tree produced by toniParser#branch.
    def enterBranch(self, ctx:toniParser.BranchContext):
        pass

    # Exit a parse tree produced by toniParser#branch.
    def exitBranch(self, ctx:toniParser.BranchContext):
        pass


    # Enter a parse tree produced by toniParser#piece.
    def enterPiece(self, ctx:toniParser.PieceContext):
        pass

    # Exit a parse tree produced by toniParser#piece.
    def exitPiece(self, ctx:toniParser.PieceContext):
        pass


    # Enter a parse tree produced by toniParser#quantifier.
    def enterQuantifier(self, ctx:toniParser.QuantifierContext):
        pass

    # Exit a parse tree produced by toniParser#quantifier.
    def exitQuantifier(self, ctx:toniParser.QuantifierContext):
        pass


    # Enter a parse tree produced by toniParser#quantity.
    def enterQuantity(self, ctx:toniParser.QuantityContext):
        pass

    # Exit a parse tree produced by toniParser#quantity.
    def exitQuantity(self, ctx:toniParser.QuantityContext):
        pass


    # Enter a parse tree produced by toniParser#quantRange.
    def enterQuantRange(self, ctx:toniParser.QuantRangeContext):
        pass

    # Exit a parse tree produced by toniParser#quantRange.
    def exitQuantRange(self, ctx:toniParser.QuantRangeContext):
        pass


    # Enter a parse tree produced by toniParser#quantMin.
    def enterQuantMin(self, ctx:toniParser.QuantMinContext):
        pass

    # Exit a parse tree produced by toniParser#quantMin.
    def exitQuantMin(self, ctx:toniParser.QuantMinContext):
        pass


    # Enter a parse tree produced by toniParser#quantMax.
    def enterQuantMax(self, ctx:toniParser.QuantMaxContext):
        pass

    # Exit a parse tree produced by toniParser#quantMax.
    def exitQuantMax(self, ctx:toniParser.QuantMaxContext):
        pass


    # Enter a parse tree produced by toniParser#atom.
    def enterAtom(self, ctx:toniParser.AtomContext):
        pass

    # Exit a parse tree produced by toniParser#atom.
    def exitAtom(self, ctx:toniParser.AtomContext):
        pass


    # Enter a parse tree produced by toniParser#charClass.
    def enterCharClass(self, ctx:toniParser.CharClassContext):
        pass

    # Exit a parse tree produced by toniParser#charClass.
    def exitCharClass(self, ctx:toniParser.CharClassContext):
        pass


    # Enter a parse tree produced by toniParser#charClassExpr.
    def enterCharClassExpr(self, ctx:toniParser.CharClassExprContext):
        pass

    # Exit a parse tree produced by toniParser#charClassExpr.
    def exitCharClassExpr(self, ctx:toniParser.CharClassExprContext):
        pass


    # Enter a parse tree produced by toniParser#charGroup.
    def enterCharGroup(self, ctx:toniParser.CharGroupContext):
        pass

    # Exit a parse tree produced by toniParser#charGroup.
    def exitCharGroup(self, ctx:toniParser.CharGroupContext):
        pass


    # Enter a parse tree produced by toniParser#posCharGroup.
    def enterPosCharGroup(self, ctx:toniParser.PosCharGroupContext):
        pass

    # Exit a parse tree produced by toniParser#posCharGroup.
    def exitPosCharGroup(self, ctx:toniParser.PosCharGroupContext):
        pass


    # Enter a parse tree produced by toniParser#charRange.
    def enterCharRange(self, ctx:toniParser.CharRangeContext):
        pass

    # Exit a parse tree produced by toniParser#charRange.
    def exitCharRange(self, ctx:toniParser.CharRangeContext):
        pass


    # Enter a parse tree produced by toniParser#seRange.
    def enterSeRange(self, ctx:toniParser.SeRangeContext):
        pass

    # Exit a parse tree produced by toniParser#seRange.
    def exitSeRange(self, ctx:toniParser.SeRangeContext):
        pass


    # Enter a parse tree produced by toniParser#charOrEsc.
    def enterCharOrEsc(self, ctx:toniParser.CharOrEscContext):
        pass

    # Exit a parse tree produced by toniParser#charOrEsc.
    def exitCharOrEsc(self, ctx:toniParser.CharOrEscContext):
        pass


    # Enter a parse tree produced by toniParser#charClassEsc.
    def enterCharClassEsc(self, ctx:toniParser.CharClassEscContext):
        pass

    # Exit a parse tree produced by toniParser#charClassEsc.
    def exitCharClassEsc(self, ctx:toniParser.CharClassEscContext):
        pass


    # Enter a parse tree produced by toniParser#catEsc.
    def enterCatEsc(self, ctx:toniParser.CatEscContext):
        pass

    # Exit a parse tree produced by toniParser#catEsc.
    def exitCatEsc(self, ctx:toniParser.CatEscContext):
        pass


    # Enter a parse tree produced by toniParser#complEsc.
    def enterComplEsc(self, ctx:toniParser.ComplEscContext):
        pass

    # Exit a parse tree produced by toniParser#complEsc.
    def exitComplEsc(self, ctx:toniParser.ComplEscContext):
        pass


    # Enter a parse tree produced by toniParser#charProp.
    def enterCharProp(self, ctx:toniParser.CharPropContext):
        pass

    # Exit a parse tree produced by toniParser#charProp.
    def exitCharProp(self, ctx:toniParser.CharPropContext):
        pass



del toniParser