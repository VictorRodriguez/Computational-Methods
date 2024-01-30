%{

#include <stdlib.h>

#include <stdio.h>

#include <string.h>





int yylex();

void yyerror(const char *s);

extern FILE *yyin;

int valid_expression = 1;

%}



%token ARTICLE NOUN VERB PREP EOL



%%

sentences : sentence

          | sentences EOL sentences

          ;

sentence : noun_phrase verb_phrase { printf("approved\n"); }

noun_phrase : cmplx_noun | cmplx_noun prep_phrase;

verb_phrase : cmplx_verb | cmplx_verb prep_phrase;

prep_phrase : PREP cmplx_noun;

cmplx_noun : ARTICLE NOUN;

cmplx_verb : VERB | VERB noun_phrase;

%%



void yyerror(const char *s) {

    valid_expression = 0;

    printf("Error\n");

}



int main(int argc, char* *argv) {

    FILE *input = fopen(argv[1], "r");

    if (input == NULL) {

        printf("file not found\n");

        return 1;

    }

    yyin = input;

    yyparse();

    fclose(input);

    return 0;

}

