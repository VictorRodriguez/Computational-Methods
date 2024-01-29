%{
#include <stdio.h>
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

int main() {
    int estado = yyparse();
    if (estado == 0) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
    }
    return estado;
}

