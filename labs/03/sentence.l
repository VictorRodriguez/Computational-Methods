%{
#include "y.tab.h"
extern int yylval;
%}
%%
"a"|"the"			 return ARTICLE; 
"with"				 return PREP; 
"boy"|"girl"|"flower"		 return NOUN; 
"touches"|"likes"|"sees"	 return VERB; 
[ \t] ; 			/* ignore whitespace */
\n return 0; 		/* logical EOF */
. return yytext[0];
%%
