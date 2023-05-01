%{
#include<stdio.h>
#include "y.tab.h"
extern int yylval;

%}

%%

a	{ return ARTICLE; }
the	{ return ARTICLE; }

boy	{ return NOUN; }
girl	{ return NOUN; }
flower	{ return NOUN; }

touches { return VERB; }
likes	{ return VERB; }
sees	{ return VERB;}
with	{ return PREP; }
[\t];
[\n]	{ return EOL; }
.	{}
%%

int yywrap()
{
	return 1;
}	
