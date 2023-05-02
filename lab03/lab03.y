%{ 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREPOSITION EOL

%%

sentences: sentence     { printf("PASS \n");}
          |sentences EOL sentences
          |sentences EOL
;

sentence: noun_phrase verb_phrase
;

noun_phrase: complex_noun
             |complex_noun prep_phrase
;

verb_phrase: complex_verb
             |complex_verb prep_phrase
;

prep_phrase: PREPOSITION complex_noun
;

complex_noun: ARTICLE NOUN
;

complex_verb: VERB
              |VERB noun_phrase
;

%%



int main(int argc, char **argv){
    if (argc != 2){
        printf("The program is not being passed the correct number of arguments");
        exit(1); 
    }

    // FILE *test = fopen(argv[1], "r");

    // yyin = test;
    yyin = fopen(argv[1], "r");
    yyparse();
}

void yyerror(const char *s){
    printf("FAIL\n");
}

