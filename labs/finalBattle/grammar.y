%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    void yyerror(const char *s);
    int yylex(void);
%}

%token ARTICLE NOUN VERB PREP EOL

%start SENTENCE


%%

SENTENCE    : NOUN_PHRASE VERB_PHRASE EOL
            ;

NOUN_PHRASE : ARTICLE NOUN
            | ARTICLE NOUN PREP_PHRASE
            ;

VERB_PHRASE : VERB
            | VERB ARTICLE NOUN
            | VERB ARTICLE NOUN PREP_PHRASE
            ;

PREP_PHRASE : PREP ARTICLE NOUN
            ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

void checkIfSuccessful() {
    int state = yyparse();
    if (state == 0){
        printf("PASS\n");
    }else{
        printf("FAIL\n");
    }
}
