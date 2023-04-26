%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP EOL
%%

sentences: sentence                             {printf("PASS \n");}
 | sentences EOL sentences
 | sentences EOL
 ;

sentence: noun_phrase verb_phrase
 ;

noun_phrase: cmplx_noun
 | cmplx_noun prep_phrase                        
 ;

verb_phrase: cmplx_verb
 | cmplx_verb prep_phrase
 ;

prep_phrase: prep cmplx_noun
 ;

cmplx_noun: article noun
 ;

cmplx_verb: verb
 | verb noun_phrase
 ;

article: ARTICLE
 ;

noun: NOUN
 ;

verb: VERB
 ;

prep: PREP
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
    printf("FAIL \n");
}