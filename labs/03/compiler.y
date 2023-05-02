%{
#include <stdio.h>
#include <stdbool.h>

int yylex();
void yyerror(const char* s);
extern FILE* yyin;
extern char* yytext;

bool pass = true;

%}

%token ARTICLE NOUN VERB PREP EOL

%start SENTENCE_LIST

%%

SENTENCE_LIST: SENTENCE { }
             | SENTENCE_LIST EOL SENTENCE { }
             ;

SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("---PASS---\n"); }
        | NOUN_PHRASE VERB_PHRASE NOUN_PHRASE { printf("---PASS---\n"); }
	| NOUN_PHRASE VERB_PHRASE NOUN_PHRASE PREP_PHRASE { printf("---PASS---\n"); }
	| CMPLX_NOUN { printf("---PASS---\n"); }
	| CMPLX_NOUN PREP_PHRASE { printf("---PASS---\n"); }
        ;

NOUN_PHRASE: CMPLX_NOUN
	   | CMPLX_NOUN PREP_PHRASE
           ;

VERB_PHRASE: CMPLX_VERB 
           | CMPLX_VERB PREP_PHRASE
           ;

PREP_PHRASE: PREP CMPLX_NOUN
            ;

CMPLX_NOUN: ARTICLE NOUN
          | ARTICLE NOUN PREP_PHRASE
          ;

CMPLX_VERB: VERB 
          | VERB NOUN_PHRASE
          ;

%%

void yyerror(const char* s) {
    printf("---FAIL---\n");
    pass = false;
}

int main(int argc, char* argv[]) {
	if (argc > 1) {
		FILE* file = fopen(argv[1], "r");
		if (!file) {
			printf("Error opening file\n");
			return 1;
		}
		yyin = file;
	}
	yyparse();
	return pass ? 0 : 1;
}
