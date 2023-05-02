%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}


%token ARTICLE NOUN VERB PREP EOL

%%

sentences: sentence	{ printf("PASS\n"); }
         | sentences EOL sentences
         | sentences EOL
         ;

sentence: noun_phrase verb_phrase		
;

noun_phrase: complex_noun | complex_noun prep_phrase
;

verb_phrase: complex_verb | complex_verb prep_phrase
;

prep_phrase: PREP complex_noun
;

complex_noun: ARTICLE NOUN
;

complex_verb: VERB | VERB noun_phrase
;

%%

void yyerror(const char *s){
    printf("FAIL\n");
}

int main(int argc, char **argv){
    if (argc != 2){
        printf("Couldn't Open File: \n");
        fprintf(stderr, "Missing: %s <filename>\n", argv[0]);
        exit(1);
    }
    
    FILE *input = fopen(argv[1],"r");
    if (!input){
        exit(1);
    }

    yyin = input;
    yyparse();
    fclose(input);


    return 0;
}

