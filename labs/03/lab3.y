%{
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN PREP VERB EOL 
%%

sentences: sentence { printf("PASS\n");}
| sentences EOL sentences
| sentences EOL
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
| VERB nounphrase;

%%

void yyerror(const char *s){
	printf("FAIL\n");
}

int main(int argc, char **argv) {
    if (argc != 2) {
	 printf("Using: %s filename\n", argv[0]);
		 return 1;
   }

    FILE* input  = fopen(argv[1], "r");
    if (!input) {
        perror("fopen");
        return 1;
    }

    yyin = input;
    yyparse();

    fclose(input);
    return 0;
}

