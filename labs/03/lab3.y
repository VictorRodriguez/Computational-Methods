%{
#include <stdio.h>
#include <stdlib.h>
extern FILE *yyin;
int yylex();
void yyerror(char *e);
%}

%token ARTICLE NOUN VERB PREP EOL

%%
    SENTENCES: SENTENCE | SENTENCES EOL {printf("sente eol");}| SENTENCES EOL SENTENCES {printf("sente eol sente");}| EOL SENTENCES {printf("eol sente");};
    SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("PASS\n");};
    NOUN_PHRASE: CMPLX_NOUN | CMPLX_NOUN PREP_PHRASE;
    PREP_PHRASE: PREP CMPLX_NOUN;
    VERB_PHRASE: CMPLX_VERB | CMPLX_VERB PREP_PHRASE;
    CMPLX_NOUN: ARTICLE NOUN;
    CMPLX_VERB: VERB | VERB NOUN_PHRASE;
%%

void yyerror(char *e){
    printf("FAIL\n");
}
int yywrap() {
    return 1;
}
int main(int argc, char **argv){
    FILE *file = fopen(argv[1],"r");
    if(!file || argc != 2){
        printf("Error File Not Found");
        return -1;
    }
    yyin = file;
    yyparse();
    fclose(file);
    return 0;
}
