%{
#include <stdlib.h>
#include <stdio.h>

int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP EOL

%%

sentences: sentence { printf("PASS\n");}
    | sentences EOL sentences
    | sentences EOL;

sentence: nounPhrase verbPhrase;

nounPhrase: complexNoun            
    | complexNoun prepPhrase;

complexNoun: ARTICLE NOUN;

complexVerb: VERB                
    | VERB nounPhrase;

prepPhrase: PREP complexNoun;

verbPhrase: complexVerb             
    | complexVerb prepPhrase;

%%

void yyerror(const char *s){
    printf("FAIL\n");
}

int main(int argc, char **argv){
    if(argc!=2){
        fprintf(stderr,"Cant open");
        exit(1);
    }

    FILE *input=fopen(argv[1],"r");
    if(!input){
        perror("fopen");
        exit(1);
    }
    yyin=input;
    yyparse();
    fclose(input);

    return 0;
}

