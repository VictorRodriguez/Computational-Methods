%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP
%%

sentence: nounPhrase verbPhrase		{printf("Valid Sentence\n");}
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
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (yyin == NULL) {
            perror(argv[1]);
            exit(1);
        }
    }
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}
