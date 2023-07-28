all:
	yacc -d grammar.y
	lex simple_lex.l
	gcc y.tab.c lex.yy.c -ly -ll -o compiler
clean:
	rm -rf lex.yy.c
	rm -rf y.tab.c
	rm -rf y.tab.h
	rm -rf y.tab.h.gch
	rm -rf instructions.asm