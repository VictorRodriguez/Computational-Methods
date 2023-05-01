%{
#include <stdio.h>
#include <stdbool.h>

int yylex();
void yyerror(const char* s);
extern FILE* yyin;
extern char* yytext;

bool pass = true;

%}

%error-verbose

%token ARTICLE NOUN VERB PREP EOL

%start sentence_list

%%
sentence_list: sentence {}
	| sentence_list EOL sentence {}
	;

sentence: noun_phrase verb_phrase { printf("PASS\n"); }
        | noun_phrase verb_phrase noun_phrase { printf("PASS\n"); }
        | noun_phrase verb_phrase noun_phrase prep_phrase { printf("PASS\n"); }
        | cmplx_noun { printf("PASS\n"); }
        | cmplx_noun prep_phrase { printf("PASS\n"); }
        ;

noun_phrase: cmplx_noun { }
           | cmplx_noun prep_phrase { }
           ;

verb_phrase: cmplx_verb { }
           | cmplx_verb prep_phrase { }
           ;

prep_phrase: prep cmplx_noun { }

cmplx_noun: article noun { }
          | article noun prep_phrase { }
          ;

cmplx_verb: verb { }
          | verb noun_phrase { }
          ;

article: ARTICLE { }
       ;

noun: NOUN { }
    ;

verb: VERB { }
    ;

prep: PREP { }
    ;

%%

void yyerror(const char* s) {
    printf("Syntax error: %s at token %s\n", s, yytext);
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