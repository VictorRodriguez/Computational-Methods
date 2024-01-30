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

/* Regla inicial */
start: sentences '\n' { printf("Sentence is valid.\n"); }

/* Producción recursiva para manejar múltiples oraciones */
sentences: /* empty */
          | sentences sentence '\n' { printf("Sentence is valid.\n"); }

/* Definición de una oración */
sentence: NOUN_PHRASE VERB_PHRASE { printf("Complete sentence: %s %s\n", $1, $2); }
        | NOUN_PHRASE { printf("Noun phrase: %s\n", $1); }
        | VERB_PHRASE { printf("Verb phrase: %s\n", $1); }
;

/* Definición de una frase nominal */
NOUN_PHRASE: ARTICLE NOUN { $$ = strdup(strcat($1, $2)); }
           | ARTICLE NOUN PREP_PHRASE { $$ = strdup(strcat(strcat($1, $2), $3)); }
;

/* Definición de una frase verbal */
VERB_PHRASE: VERB { $$ = strdup($1); }
           | VERB NOUN_PHRASE { $$ = strdup(strcat($1, $2)); }
;

/* Definición de una frase preposicional */
PREP_PHRASE: PREP NOUN_PHRASE { $$ = strdup(strcat($1, $2)); }
;

%%

/* Función de manejo de errores */
void yyerror(const char *s) {
    fprintf(stderr, "Syntax error at line %d: %s\n", line_number, s);
}

/* Función principal */
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
