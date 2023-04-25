%{
#include "y.tab.h"
%}
%%
"a"|"the"			 return ARTICLE; 
"with"				 return PREP; 
"boy"|"girl"|"flower"		 return NOUN; 
"touches"|"likes"|"sees"	 return VERB; 
[ \t] ; 			/* ignore whitespace */
[\n]  ; 		return EOL;
. return yytext[0];
%%