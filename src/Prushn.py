#!/usr/bin/env python3

import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from PrushnLexer import PrushnLexer
from PrushnParser import PrushnParser
from PrushnReader import PrushnReader
from PrushnListener import PrushnListener

def main(argv):
    with open("Uttar.md", "w") as output_stream:
        input_stream = FileStream(argv[1])

        lexer = PrushnLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PrushnParser(stream)
        tree = parser.program()
        walker = ParseTreeWalker()
        walker.walk(PrushnReader(parser, output_stream), tree)

if __name__ == '__main__':
    main(sys.argv)
