%{
#include "y.tab.h"
extern FILE* yyin;
extern FILE* yyout;
%}

%%

[ \t\n]           ; // Ignore whitespace and newlines

"Robot"           { return ROBOT; }
"please"          { return PLEASE; }
"move"            { return MOVE; }
"ahead"           { return AHEAD; }
"and"             { return AND; }
"then"            { return THEN; }
"turn"            { return TURN; }
[0-9]+            { yylval.num = atoi(yytext); return NUMBER; }

"blocks"          { return BLOCKS; }
"degrees"         { return DEGREES; }

.                 { return yytext[0]; } // Any other character

%%

int yywrap() {
    return 1;
}

