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

sentences: sentence                  {printf("PASS\n");}
 | sentences EOL sentences
 | sentences EOL
 ;

sentence: nounPhrase verbPhrase		
;

nounPhrase: cmplxNoun
 | cmplxNoun prepPhrase
;
verbPhrase: cmplxVerb
 | cmplxVerb prepPhrase
;
prepPhrase: PREP cmplxNoun
;
cmplxNoun: ARTICLE NOUN
;
cmplxVerb: VERB
 | VERB nounPhrase
;

%%

int main(int argc, char **argv) {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (yyin == NULL) {
            perror(argv[1]);
            exit(1);
        }
    }
    yyparse();
}

void yyerror(const char *s) {
    printf("FAIL\n");
}
