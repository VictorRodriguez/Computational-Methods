%{
#include "grammar_yacc.tab.h"
%}

%%

with    { return PREP; }
a|the   { return ARTICLE; }
boy|girl|flower   { return NOUN; }
touches|likes|sees   { return VERB; }
[ \t\n]         ;  /* Ignore whitespace */

.               { return yytext[0]; }

%%

int yywrap() {
    return 1;
}

