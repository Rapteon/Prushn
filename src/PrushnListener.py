# Generated from Prushn.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrushnParser import PrushnParser
else:
    from PrushnParser import PrushnParser

# This class defines a complete listener for a parse tree produced by PrushnParser.
class PrushnListener(ParseTreeListener):

    # Enter a parse tree produced by PrushnParser#program.
    def enterProgram(self, ctx:PrushnParser.ProgramContext):
        pass

    # Exit a parse tree produced by PrushnParser#program.
    def exitProgram(self, ctx:PrushnParser.ProgramContext):
        pass


    # Enter a parse tree produced by PrushnParser#question.
    def enterQuestion(self, ctx:PrushnParser.QuestionContext):
        pass

    # Exit a parse tree produced by PrushnParser#question.
    def exitQuestion(self, ctx:PrushnParser.QuestionContext):
        pass


    # Enter a parse tree produced by PrushnParser#text.
    def enterText(self, ctx:PrushnParser.TextContext):
        pass

    # Exit a parse tree produced by PrushnParser#text.
    def exitText(self, ctx:PrushnParser.TextContext):
        pass



del PrushnParser