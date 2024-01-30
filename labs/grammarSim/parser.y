%{
#include <stdio.h>
%}

%token ARTICLE NOUN VERB PREP

%%

line: NOUN_PHRASE VERB_PHRASE '\n' { printf("PASS\n"); }
    | '\n' { /* Empty line, do nothing */ }
    | error '\n' { printf("FAIL\n"); }
    ;

NOUN_PHRASE: CMPLX_NOUN { /* Additional actions if needed */ }
           ;

VERB_PHRASE: CMPLX_VERB { /* Additional actions if needed */ }
           | CMPLX_VERB PREP_PHRASE { /* Additional actions if needed */ }
           ;

CMPLX_NOUN: ARTICLE NOUN { /* Additional actions if needed */ }
          ;

CMPLX_VERB: VERB { /* Additional actions if needed */ }
          | VERB CMPLX_NOUN { /* Additional actions if needed */ }
          ;

PREP_PHRASE: PREP CMPLX_NOUN { /* Additional actions if needed */ }
           ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

