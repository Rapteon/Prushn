from PrushnListener import PrushnListener
from PrushnParser import PrushnParser
from Search import GoogleSearch
from typing import TextIO

class PrushnReader(PrushnListener):
    def __init__(self, parser:PrushnParser, output_stream: TextIO):
        self.parser = parser
        self.question_answer = dict()
        self.searcher = GoogleSearch(output_stream)

    # Enter a parse tree produced by PrushnParser#program.
    def enterProgram(self, ctx:PrushnParser.ProgramContext):
        # Store results based on question number. Also check if question numbers are unique.
        # May require changes in grammar
        print('Entered program')

    # Exit a parse tree produced by PrushnParser#program.
    def exitProgram(self, ctx:PrushnParser.ProgramContext):
        print("exited program")


    # Enter a parse tree produced by PrushnParser#question.
    def enterQuestion(self, ctx:PrushnParser.QuestionContext):
        print('Entered question')

    # Exit a parse tree produced by PrushnParser#question.
    def exitQuestion(self, ctx:PrushnParser.QuestionContext):
        print("exited question")

    # Enter a parse tree produced by PrushnParser#text.
    def enterText(self, ctx:PrushnParser.TextContext):
        search_words = self.parser.getTokenStream().getText(ctx.start, ctx.stop)
        self.searcher.search(search_words)

    # Exit a parse tree produced by PrushnParser#text.
    def exitText(self, ctx:PrushnParser.TextContext):
        print("exited text")

