%{
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int yylex();
void yyerror (const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP EOL
%%

lines: sentence {printf("PASS \n");}
| lines EOL lines
| lines EOL
;

sentence: nounphrase verbphrase
;

nounphrase: cmplxnoun 
| cmplxnoun prepphrase
;

verbphrase: cmplxverb 
| cmplxverb prepphrase
;

prepphrase: PREP cmplxnoun
;

cmplxnoun: ARTICLE NOUN
;

cmplxverb: VERB
| VERB nounphrase
;

%%

void yyerror(const char *s){
	printf("FAIL \n");
}

int main(int argc, char** argv){
	if(argc!=2){
		fprintf(stderr, "Cannot open file");
		exit(1);
	}
	
	FILE* input = fopen(argv[1], "r");
	if(!input){
		perror("fopen");	
		exit(1);
	}

	yyin = input;
	yyparse();
	fclose(input);
	return 0;
}
