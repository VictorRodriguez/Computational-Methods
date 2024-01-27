%{
#include "y.tab.h"
extern int yylval;
%}
%%
"boy"|"girl"|"flower"			{ yylval = yytext[0]; return NOUN;}
"a"|"the"			{ yylval = yytext[0]; return ARTICLE;}
"touches"|"likes"|"sees"	{ yylval = yytext[0]; return VERB;}
"with"				{ yylval = yytext[0]; return PREP;}
[\t];				/* ignore whitespace*/
\n return 0;			/*Logical EOF*/
. return yytext[0];
%%
