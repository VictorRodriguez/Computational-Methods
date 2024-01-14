/* 

Lab3
Nolberto Castro Sánchez 
A01641501 

 */

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
| SENTENCES EOL
;

SENTENCE: NOUN_PHRASE VERB_PHRASE
;

NOUN_PHRASE: COMPLEX_NOUN		        
| COMPLEX_NOUN PREP_PHRASE
;
PREP_PHRASE: PREP COMPLEX_NOUN
;

VERB_PHRASE: COMPLEX_VERB             
| COMPLEX_VERB PREP_PHRASE
;

COMPLEX_NOUN: ARTICLE NOUN
;

COMPLEX_VERB: VERB		            
| VERB NOUN_PHRASE
;

%%

int main(int argc, char **argv){
	if(argc!=2){
		fprintf(stderr,"Cant open");
		exit(1);
	}

	FILE *file=fopen(argv[1],"r");
	if(!file){
		perror("fopen");
		exit(1);
	}
	yyin=file;
	yyparse();
	fclose(file);

	return 0;
}

void yyerror(const char *s){
	printf("FAIL\n");
}