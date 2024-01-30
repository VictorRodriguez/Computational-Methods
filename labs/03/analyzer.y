/* 	
	STUDENT INFORMATION
	
	Rodrigo López Guerra
	A01737437

	Laboratorio 3.

	YACC Syntax Interpreter
*/

/* 	DEFINICIONES     */ 

%{
#include <stdio.h>

extern FILE *yyin;

void yyerror(const char *s);
int yylex(void);

int set = 0;
%}

/* 	IDENTIFICADORES     */ 

%token ARTICLE NOUN GNOUN VERB PREP EOL
%start INPUT

/* 	REGLAS     */ 

%%

/* Reglas de la Gramática Adaptada */

INPUT: 					/* Espacio en blanco */ 
	    					| EOL {/* Ignora espacios en blanco */ ;}
            					| INPUT SENTENCE {set = 0;}
	    					| INPUT error EOL { yyerrok; printf("FAIL\n"); set=0; }
            					;

SENTENCE:				NOUN_PHRASE VERB_PHRASE EOL { printf("PASS\n"); set=1; }
            					;

NOUN_PHRASE : 			CMPLX_NOUN
            					| CMPLX_NOUN PREP_PHRASE
            					;

PREP_PHRASE: 			PREP CMPLX_NOUN 
						| PREP CMPLX_GNOUN 
            					;

VERB_PHRASE : 			VERB
	    					| VERB CMPLX_GNOUN
            					| VERB NOUN_PHRASE
            					;

CMPLX_NOUN  : 			ARTICLE NOUN
            					;

CMPLX_GNOUN: 			ARTICLE GNOUN
						;

%%

/* 	ERRORES GENERADOS     */ 

void yyerror(const char *s) {
}

/* 	PROGRAMA PRINCIPAL     */ 

int main(int argc, char **argv) {

	FILE *fd;  // Declaración de la variable fd

	if (argc == 2) {
		fd = fopen(argv[1], "r");
        	if (!fd){
            		perror("Error: ");
            		return (-1);
        	}
        	yyin = fd;  // Establecer yyin para leer del archivo
    	}
    	else {
        	printf("Usage: ./analyzer FILENAME\n");
        	return 1;  // Retornar con error si no se proporciona el nombre del archivo
    	}

	int result = yyparse();
	if (set != 1){
    		printf("FAIL\n"); // Se pone este comparador ya que al finalizar todas las reglas, YACC es incapaz de devolver la regla para un error.
	}

    	if (fd != NULL) {
        	fclose(fd);  // Cerrar el archivo si está abierto
    	}

	return 0;
}
