%{
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREPOSITION EOL

%%

sentences
    : /* empty */
    | sentences sentence EOL { printf("PASS\n"); }
    | sentences error EOL    { printf("FAIL\n"); yyerrok; yyclearin; }
    ;

sentence
    : noun_phrase verb_phrase
    ;

noun_phrase
    : ARTICLE NOUN
    | ARTICLE NOUN prep_phrase
    ;

verb_phrase
    : VERB
    | VERB noun_phrase
    | VERB prep_phrase
    ;

prep_phrase
    : PREPOSITION noun_phrase
    ;

%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        exit(1);
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror(argv[1]);
        exit(1);
    }
    
    do {
        yyparse();
    } while (!feof(yyin));

    fclose(yyin);
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

