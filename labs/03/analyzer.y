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
 
SENTENCES: SENTENCE	{ printf("PASS\n"); };
| SENTENCES EOL SENTENCES
| SENTENCES EOL
;

SENTENCE: NOUN_PHRASE VERB_PHRASE
;

NOUN_PHRASE: CMPLX_NOUN
| CMPLX_NOUN PREP_PHRASE
;

VERB_PHRASE: CMPLX_VERB
| CMPLX_VERB PREP_PHRASE
;

CMPLX_NOUN: ARTICLE NOUN
;

CMPLX_VERB: VERB
| VERB NOUN_PHRASE
;

PREP_PHRASE: PREP CMPLX_NOUN
;

%%

void yyerror(const char *s) {
	printf("FAIL\n");
}

int main(int argc, char **argv) {
    if (argc != 2) {
	fprintf(stderr, "Cant open");
	exit(1);
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
	perror("fopen");
	exit(1);
    }
    yyparse();
    fclose(yyin);
    return 0;
}
         


