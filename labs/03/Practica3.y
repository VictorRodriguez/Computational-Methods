%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
extern int line_number;
extern FILE *yyin;
extern int yylex();
void yyerror(const char *s);
%}

%union {
    char *sval;
}

%token <sval> ARTICLE NOUN VERB PREP

%%

start: sentences '\n' { printf("PASS\n"); }


sentences: /* empty */
          | sentences sentence '\n'

sentence: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); }
        | NOUN_PHRASE { printf("PASS\n"); }
        | VERB_PHRASE { printf("PASS\n"); }

NOUN_PHRASE: ARTICLE NOUN
           | ARTICLE NOUN PREP_PHRASE
;

VERB_PHRASE: VERB
           | VERB NOUN_PHRASE
;

PREP_PHRASE: PREP NOUN_PHRASE
;


%%

void yyerror(const char *s) {
    fprintf(stderr, "FAIL... FIN DE ARCHIVO\n");
}

int main(int argc, char **argv) {
    if (argc == 2) {
        if (!(yyin = fopen(argv[1], "r"))) {
            perror("Error al abrir el archivo: ");
            return 1;
        }

        yyparse();
        fclose(yyin);
        
    } else {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        return 1;
    }

    return 0;
}
