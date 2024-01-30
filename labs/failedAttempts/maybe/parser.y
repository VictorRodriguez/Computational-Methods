%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);

%}

%union {
    char *str;
}

%token <str> NOUN ARTICLE VERB PREP

%%

SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); }
        | error { printf("FAIL\n"); }
        ;

VERB_PHRASE: CMPLX_VERB | CMPLX_VERB PREP_PHRASE;

NOUN_PHRASE: NOUN | CMPLX_NOUN | CMPLX_NOUN PREP_PHRASE;

CMPLX_NOUN: ARTICLE NOUN { printf("Noun: %s\n", $2); };

CMPLX_VERB: VERB { printf("Verb: %s\n", $1); }
         | VERB CMPLX_NOUN { printf("Verb: %s\n", $1); };

PREP_PHRASE: PREP CMPLX_NOUN;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    exit(EXIT_FAILURE);
}

int main() {
    yyparse();
    return 0;
}

