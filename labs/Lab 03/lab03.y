%{
#include <stdio.h>
%}

%token ARTICLE NOUN VERB PREP

%%
SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); }
        ;

NOUN_PHRASE: CMPLX_NOUN
           | CMPLX_NOUN PREP_PHRASE
           ;

VERB_PHRASE: CMPLX_VERB
           | CMPLX_VERB PREP_PHRASE
           ;

PREP_PHRASE: PREP CMPLX_NOUN
           ;

CMPLX_NOUN: ARTICLE NOUN
          ;

CMPLX_VERB: VERB
          | VERB NOUN_PHRASE
          ;

ARTICLE: 'a'
       | 'the'
       ;

NOUN: 'boy'
     | 'girl'
     | 'flower'
     ;

VERB: 'touches'
     | 'likes'
     | 'sees'
     ;

PREP: 'with'
     ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char* s) {
    printf("FAIL\n");
    return 0;
}
