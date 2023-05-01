all:
	
	yacc -d grammar.y
	lex tokens.l
	gcc y.tab.c lex.yy.c -ly -ll -o analyzer


clean:
	rm -rf analyzer
	rm -rf y.tab.c
	rm -rf lex.yy.c
	rm -rf y.tab.h
	rm -rf y.tab.h.gch

