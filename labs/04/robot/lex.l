%{
#include <stdio.h>
#include "y.tab.h"
%}
%%

Robot                           { return ROBOT; }

please                          { return PLEASE; }

turn                            { return TURN; }

move                            { return MOVE; }

90|180|270|360                  { yylval = atoi(yytext); return DEGREES_NUMBER; }

(blocks\ ahead)|blocks          { return BLOCKS; }

[0-9]                           { yylval = atoi(yytext); return BLOCKS_NUMBER; }

degrees                         { return DEGREES; }

(,\ )?((and\ then)|then|and)    { return THEN; }

\/\/[ -~]*                      /* comentario */;

[ \t]+                          /* espacio */;
%%
