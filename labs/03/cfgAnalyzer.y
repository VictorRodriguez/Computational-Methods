%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern char* yytext;
extern FILE* yyin;

void yyerror(const char *s) {
    fprintf(stderr, "ERROR: %s\n", s);
    exit(0);
}

%}

%token ARTICLE NOUN VERB PREPOSITION 
%start SENTENCE

%%
SENTENCE : NOUN_PHRASE VERB_PHRASE
        ;
NOUN_PHRASE : CMPLX_NOUN
            | CMPLX_NOUN PREPOSITION_PHRASE
            ;
VERB_PHRASE : CMPLX_VERB
            | CMPLX_VERB PREPOSITION_PHRASE
            ;
PREPOSITION_PHRASE : PREPOSITION CMPLX_NOUN
            ;
CMPLX_NOUN : ARTICLE NOUN
            | ARTICLE PREPOSITION_PHRASE
            ;
CMPLX_VERB : VERB 
            | VERB NOUN_PHRASE
        ;

%%

int main(int argc, char **argv) {


    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror(argv[1]);
        exit(1);
    }

    yyin = f;

    int parseResult;

    while ((parseResult = yyparse()) != 0) {
        switch(parseResult) {
            case 1:
                printf("PASS\n");
            break;
            default:
                printf("FAIL\n");
            break;
        }
    }

    fclose(f);
    return 0;
}

int yywrap() {
    return 1;
}
