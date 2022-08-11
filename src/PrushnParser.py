# Generated from Prushn.g4 by ANTLR 4.10.1
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
        4,1,10,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,4,2,19,8,2,11,2,12,2,20,1,2,0,0,3,0,2,4,
        0,0,21,0,7,1,0,0,0,2,11,1,0,0,0,4,18,1,0,0,0,6,8,3,2,1,0,7,6,1,0,
        0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,5,1,
        0,0,12,13,3,4,2,0,13,14,5,3,0,0,14,15,5,2,0,0,15,3,1,0,0,0,16,17,
        5,9,0,0,17,19,5,10,0,0,18,16,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,
        20,21,1,0,0,0,21,5,1,0,0,0,2,9,20
    ]

class PrushnParser ( Parser ):

    grammarFileName = "Prushn.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'?'" ]

    symbolicNames = [ "<INVALID>", "QUESTION_BEGIN", "NEWLINE", "QUESTION_MARK", 
                      "SPECIAL", "ALPHABET", "LETTER", "DIGIT", "NUMBER", 
                      "WORD", "SPACE" ]

    RULE_program = 0
    RULE_question = 1
    RULE_text = 2

    ruleNames =  [ "program", "question", "text" ]

    EOF = Token.EOF
    QUESTION_BEGIN=1
    NEWLINE=2
    QUESTION_MARK=3
    SPECIAL=4
    ALPHABET=5
    LETTER=6
    DIGIT=7
    NUMBER=8
    WORD=9
    SPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def question(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrushnParser.QuestionContext)
            else:
                return self.getTypedRuleContext(PrushnParser.QuestionContext,i)


        def getRuleIndex(self):
            return PrushnParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PrushnParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.question()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrushnParser.QUESTION_BEGIN):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_BEGIN(self):
            return self.getToken(PrushnParser.QUESTION_BEGIN, 0)

        def text(self):
            return self.getTypedRuleContext(PrushnParser.TextContext,0)


        def QUESTION_MARK(self):
            return self.getToken(PrushnParser.QUESTION_MARK, 0)

        def NEWLINE(self):
            return self.getToken(PrushnParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PrushnParser.RULE_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion" ):
                listener.enterQuestion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion" ):
                listener.exitQuestion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion" ):
                return visitor.visitQuestion(self)
            else:
                return visitor.visitChildren(self)




    def question(self):

        localctx = PrushnParser.QuestionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_question)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(PrushnParser.QUESTION_BEGIN)
            self.state = 12
            self.text()
            self.state = 13
            self.match(PrushnParser.QUESTION_MARK)
            self.state = 14
            self.match(PrushnParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(PrushnParser.WORD)
            else:
                return self.getToken(PrushnParser.WORD, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(PrushnParser.SPACE)
            else:
                return self.getToken(PrushnParser.SPACE, i)

        def getRuleIndex(self):
            return PrushnParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = PrushnParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.match(PrushnParser.WORD)
                self.state = 17
                self.match(PrushnParser.SPACE)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PrushnParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





