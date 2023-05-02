%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
extern int yyparse();
%}

%token ARTICLE NOUN VERB PREP EOL

%%

SENTENCE: NOUN_PHRASE VERB_PHRASE EOL { printf("PASS\n"); };

NOUN_PHRASE: CMPLX_NOUN | CMPLX_NOUN PREP_PHRASE;

VERB_PHRASE: CMPLX_VERB | CMPLX_VERB PREP_PHRASE;

PREP_PHRASE: PREP CMPLX_NOUN;

CMPLX_NOUN: ARTICLE NOUN;

CMPLX_VERB: VERB | VERB NOUN_PHRASE;

%%

void yyerror(const char *s) {
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

