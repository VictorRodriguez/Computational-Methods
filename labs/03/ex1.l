%{
#include "y.tab.h"
extern int yylval;
%}

%%
(a|the)                 { yylval = strdup(yytext); return ARTICLE;}
(boy|girl|flower)       { yylval = strdup(yytext); return NOUN;}
(touches|likes|sees)    { yylval = strdup(yytext); return VERB;}
with                    { yylval = strdup(yytext); return PREP;}
[ \t] ;                 /* ignore whitespace */
\n ;                    return EOL;
. return yytext[0];
%%