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

sentences: sentence		{ printf("PASS\n"); }
|	sentences EOL sentences
|	sentences EOL;

sentence: nounPhrase verbPhrase;

nounPhrase: complexNoun | complexNoun prepPhrase;

verbPhrase: complexVerb | complexVerb prepPhrase;

prepPhrase: PREP complexNoun;

complexNoun: ARTICLE NOUN;

complexVerb: VERB | VERB nounPhrase;

%%


void yyerror(const char *s){
	printf("FAIL\n");
}

int main(int argc, char **argv){
	if (argc != 2){
		fprintf( stderr, "Error Opening");
		exit(1);
	}

	FILE *tests = fopen( argv[1], "r");
	if(!tests){
		perror("fopen");
		exit(1);
	}
	printf("File open\n");
	yyin = tests;
	yyparse();
	fclose(tests);
	printf("File closed\n");
	return 0;

}
