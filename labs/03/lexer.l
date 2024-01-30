%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%{
int line_number = 1;
%}

%%
a|the                    {yylval.sval = strdup(yytext); return ARTICLE;}
boy|girl|flower          {yylval.sval = strdup(yytext); return NOUN;}
touches|likes|sees       {yylval.sval = strdup(yytext); return VERB;}
with                     {yylval.sval = strdup(yytext); return PREP;}

[ \t]+                   /* Ignorar espacios en blanco y tabulaciones */

^[ \t]*\n                /* Ignorar líneas en blanco */

\n                       { line_number++; return '\n'; }

.                        { fprintf(stderr, "Error: Caracter inesperado '%s' en la línea %d\n", yytext, line_number); }

%%

// Función auxiliar para liberar la memoria asignada a las cadenas.
void yystring_free(char* str) {
    if (str != NULL) {
        free(str);
    }
}

// Función principal de análisis léxico.
int yylex() {
    int token = yylex_aux();  // Obtener el token del analizador léxico generado por Flex.
    yystring_free(yylval.sval);  // Liberar memoria asignada a las cadenas después de su uso.
    return token;
}
