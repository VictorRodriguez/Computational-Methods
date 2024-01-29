CC = gcc
LEX = lex
YACC = yacc

CFLAGS = -Wall

all: pls

pls: lex.yy.c y.tab.c
	$(CC) $(CFLAGS) -o $@ lex.yy.c y.tab.c -ll -ly

lex.yy.c: grammar.l
	$(LEX) grammar.l

y.tab.c y.tab.h: grammar.y
	$(YACC) -d grammar.y

clean:
	rm -f pls lex.yy.c y.tab.c y.tab.h

