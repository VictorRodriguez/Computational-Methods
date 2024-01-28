%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void yyerror(const char *str)
{
    fprintf(stderr, "error: %s\n", str);
}

int yywrap()
{
    return 1;
}

int main(void)
{
    yyparse();
    return 0;
}
%}

%token /*INPUT*/ PREP VERB NOUN ARTICLE

%%
SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); } | error { printf("FAIL\n"); };

VERB_PHRASE: CMPLX_VERB | CMPLX_VERB PREP_PHRASE;

NOUN_PHRASE: CMPLX_NOUN | CMPLX_NOUN PREP_PHRASE;

CMPLX_NOUN: ARTICLE NOUN;

CMPLX_VERB: VERB | VERB NOUN_PHRASE;

PREP_PHRASE: PREP CMPLX_NOUN;

%%
