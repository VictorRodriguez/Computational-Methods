/* 
Daniel Flores Rdz A01734184
Fecha de modificación: 17 Nov 2023
*/

%{
#include "y.tab.h"
%}


%%
Awesomo   { return ROBOT; }
please    { return PLEASE; }
move      { return MOVE; }
turn      { return TURN; }
[0-9]+  { yylval.dval = atoi(yytext); return NUMBER; }
[ \t]     ;  /* saltamos espacios vacios */
\n        return 0;
. ;

%%