analyzer: lex.yy.c y.tab.c
	gcc lex.yy.c y.tab.c -o analyzer -ll -ly

lex.yy.c: lexer.l y.tab.h
	lex lexer.l

y.tab.c y.tab.h: parser.y
	yacc -d parser.y

clean:
	rm -f lex.yy.c y.tab.c y.tab.h analyzer

