%{
#include "y.tab.h"
%}

%%
"boy"|"girl"|"flower"  { yylval.str = strdup(yytext); return NOUN; }
"a"|"the"              { yylval.str = strdup(yytext); return ARTICLE; }
"touches"|"likes"|"sees" { yylval.str = strdup(yytext); return VERB; }
"with"                  { yylval.str = strdup(yytext); return PREP; }
.                       { return yytext[0]; }
%%

int yywrap() {
    return 1;
}

