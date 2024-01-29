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

[ \t]+                   /* ignore whitespace */
^[ \t]*\n                /* ignore blank lines */

\n                       { line_number++; return '\n'; }


%%
