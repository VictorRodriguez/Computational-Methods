%{
#include "y.tab.h"
%}

%%

"the"   	{ return ARTICLE; }
"a"    	        { return ARTICLE; }
"boy"           { return NOUN; }
"girl"	        { return NOUN; }
"flower"	{ return NOUN; }
"touches"	{ return VERB; }
"likes"		{ return VERB; }	
"sees"		{ return VERB; }
"with"		{ return PREP; }
[ \t\n]		; /* skip whitespace */
. 		{ return yytext[0]; } /* return other characters as is */

%%

int yywrap() {
	return 1;
}

