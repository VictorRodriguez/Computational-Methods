TARGET = parser
LEXER = lexer.l
PARSER = parser.y
LEX_SOURCE = lex.yy.c
YACC_SOURCE = y.tab.c
YACC_HEADER = y.tab.h

CC = gcc
CFLAGS = -Wall

$(TARGET): $(LEX_SOURCE) $(YACC_SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(LEX_SOURCE) $(YACC_SOURCE) -lfl

$(LEX_SOURCE): $(LEXER)
	flex $(LEXER)

$(YACC_SOURCE): $(PARSER)
	yacc -d $(PARSER)

clean:
	rm -f $(TARGET) $(LEX_SOURCE) $(YACC_SOURCE) $(YACC_HEADER)

