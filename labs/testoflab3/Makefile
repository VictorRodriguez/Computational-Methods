all:
	yacc -d -v grammar.y
	lex grammar.l
	gcc y.tab.c lex.yy.c -ly -lfl -o grammar

clean:
	rm -rf grammar
	rm -rf lex.yy.c
	rm -rf y.tab.c
	rm -rf y.tab.h
	rm -rf y.tab.h.gch
