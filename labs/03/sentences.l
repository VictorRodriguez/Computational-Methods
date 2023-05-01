%{
#include "y.tab.h"
#include <stdio.h>
extern int yylval;
%}
%%
a	 			{return ARTICLE; }
the				{return ARTICLE; }
with				{return PREP; }
sees				{return VERB; }
touches				{return VERB; }
likes				{return VERB; }
girl				{return NOUN; }
boy				{return NOUN; }
flower				{return NOUN; }
[ \t] ; 			/* ignore whitespace */
[\n] return EOL; 		 		/* logical EOF */
. return yytext[0];
%%
int yywrap()
{
return 1;
}
