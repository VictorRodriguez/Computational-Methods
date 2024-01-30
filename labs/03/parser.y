%{
#include <stdio.h>
%}

%token ARTICLE NOUN VERB PREP

%%

sentence: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); }
        ;

NOUN_PHRASE: CMPLX_NOUN {  }
           ;

VERB_PHRASE: CMPLX_VERB {  }
           | CMPLX_VERB PREP_PHRASE {  }
           ;

CMPLX_NOUN: ARTICLE NOUN {  }
          ;

CMPLX_VERB: VERB {  }
          | VERB CMPLX_NOUN {  }
          ;

PREP_PHRASE: PREP CMPLX_NOUN {  }
           ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    fprintf(stderr, "FAIL: %s\n", s);
    return 0;
}

