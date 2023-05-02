all:
	yacc -d analyzer.y
	lex analyzer.l
	gcc y.tab.c lex.yy.c -ly -ll -o analyzer

clean:
	rm -rf analyzer
	rm -rf lex.yy.c
	rm -rf y.tab.c
	rm -rf y.tab.h
	rm -rf y.tab.h.gch
