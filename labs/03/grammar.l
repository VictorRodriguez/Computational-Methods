%{

#include<stdio.h>

#include "y.tab.h"



extern int yylval;

%}

%%



with { return PREP; }

the { return ARTICLE; }

boy { return NOUN; }

touches { return VERB; }

a { return ARTICLE; }

flower { return NOUN; }

girl { return NOUN; }

likes { return VERB; }

sees { return VERB;}

[\n] { return EOL; }

[\t];

. {}

%%

int yywrap()

{

	return 1;

}	
