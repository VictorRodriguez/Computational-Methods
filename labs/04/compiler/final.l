%{
#include "y.tab.h"
%}

%%
"Robot please"   { return ROBOT_PLEASE; }
"move"           { return MOVE; }
"turn"           { return TURN; }
"ahead"          { return AHEAD; }
"blocks"         { return BLOCKS; }
"degrees"        { return DEGREES; }
"and then"       { return AND_THEN; }
","              { return COMMA; }
"degrees,"       { return DEGREESC; }
"blocks ahead,"  { return AHEADC; }
\n               { return NEWLINE; }
[0-9]+           { yylval = atoi(yytext); return NUMBER; }
[ \t]            ; /* Ignore whitespace */
<<EOF>>          { return EOF_TOKEN; }
.                { /* Ignore unrecognized characters */ }

%%

int yywrap() {
    return 1;
}
