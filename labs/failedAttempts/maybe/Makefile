CC = gcc
LEX = flex
YACC = yacc

CFLAGS = -Wall

# For Fedora, you might need to use the -lfl library for Flex
LIBS = -lfl

all: sentence_parser

sentence_parser: lex.yy.c y.tab.c
	$(CC) $(CFLAGS) lex.yy.c y.tab.c -o sentence_parser $(LIBS)

y.tab.c y.tab.h: parser.y
	$(YACC) -d parser.y

lex.yy.c: lexer.l
	$(LEX) lexer.l

clean:
	rm -f sentence_parser lex.yy.c y.tab.c y.tab.h

