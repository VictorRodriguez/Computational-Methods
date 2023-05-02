%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lex.yy.c"
%}

%token ARTICLE NOUN VERB PREP

%%

sentence: noun_phrase verb_phrase { printf("Sentence is valid\n"); }
       ;

noun_phrase: cmplx_noun
           | cmplx_noun prep_phrase
           ;

verb_phrase: cmplx_verb
           | cmplx_verb prep_phrase
           ;

prep_phrase: prep cmplx_noun
           ;

cmplx_noun: article noun
          | article noun_phrase
          ;

cmplx_verb: verb
          | verb noun_phrase
          ;

article: ARTICLE
       ;

noun: NOUN
    ;

verb: VERB
    ;

prep: PREP
    ;

%%

int main() {
    yyparse();
    return 0;
}

void yyerror(const char* s){
        printf("Invalid\n");
