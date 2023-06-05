%{
#include "y.tab.h"
%}

%%
Robot                   { return ROBOT; }
please                  { return PLEASE; }
move                    { return MOVE; }
blocks                  { return BLOCKS; }
ahead                   { return AHEAD; }
turn                    { return TURN; }
degrees                 { return DEGREES; }
and                     { return AND; }
then                    { return THEN; }
,                       { return COMMA; }
[0-9]                   {yylval.number = atoi(yytext); return NUMBER;}
90|180|270|360          {yylval.degree = atoi(yytext); return DEGREE;}
[ \t]+                  ;
\n                      { return EOL; }
.                       { return yytext[0]; }
%%

int yywrap(void){
        return 1;
}
