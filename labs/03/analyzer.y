%{ 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP EOL

%%

SENTENCES: SENTENCE { printf("PASS\n");}
	| SENTENCES EOL SENTENCES
	| SENTENCES EOL;

SENTENCE : NOUN_PHRASE VERB_PHRASE;

NOUN_PHRASE : CMPLX_NOUN | CMPLX_NOUN PREP_PHRASE;
VERB_PHRASE : CMPLX_VERB | CMPLX_VERB PREP_PHRASE;

PREP_PHRASE : PREP CMPLX_NOUN;
CMPLX_NOUN : ARTICLE NOUN;
CMPLX_VERB : VERB | VERB NOUN_PHRASE;

%%

void yyerror(const char *s){
	printf("FAIL\n");
}

int main(int argc, char **argv){

    FILE *fd;

     if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyin=fd;
        yyparse();
        fclose(fd);
    }

	return 0;
}