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

sentences: sentence { printf("PASS\n"); }
 | sentences EOL 
 | sentences EOL sentences 
 ;
sentence: nounPhrase verbPhrase
	 ;

nounPhrase: cmplxNoun | cmplxNoun prepPhrase 
	   ;

verbPhrase: cmplxVerb | cmplxVerb prepPhrase
	   ;

prepPhrase: PREP cmplxNoun
	   ;

cmplxNoun: ARTICLE NOUN
	  ;

cmplxVerb: VERB | VERB nounPhrase
	  ;

%%

void yyerror(const char *s) {
	printf("FAIL\n");
}

int main(int argc, char **argv) {
	FILE *input_file;

	if (argc != 2) {
		printf("Using: %s input_file\n", argv[0]);
		return 1;
	}

	input_file = fopen(argv[1], "r");
	if (!input_file) {
		perror(argv[1]);
		return 1;
	}

	yyin = input_file;
	yyparse();
	fclose(input_file);

	return 0;
}
