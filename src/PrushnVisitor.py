# Generated from Prushn.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrushnParser import PrushnParser
else:
    from PrushnParser import PrushnParser

# This class defines a complete generic visitor for a parse tree produced by PrushnParser.

class PrushnVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrushnParser#program.
    def visitProgram(self, ctx:PrushnParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrushnParser#question.
    def visitQuestion(self, ctx:PrushnParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrushnParser#text.
    def visitText(self, ctx:PrushnParser.TextContext):
        return self.visitChildren(ctx)



del PrushnParser