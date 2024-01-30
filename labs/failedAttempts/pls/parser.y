%{
#include <stdio.h>
%}

%token ARTICLE NOUN VERB PREP EOL

%%

sentence : noun_phrase verb_phrase EOL     { printf("PASS\n"); }
noun_phrase : cmplx_noun | cmplx_noun prep_phrase     { }
verb_phrase : cmplx_verb | cmplx_verb prep_phrase     { }
prep_phrase : prep cmplx_noun     { }
cmplx_noun : ARTICLE NOUN     { }
cmplx_verb : VERB | VERB noun_phrase     { }

prep : PREP     { }

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *msg) {
    fprintf(stderr, "FAIL\n");
    return 0;
}

