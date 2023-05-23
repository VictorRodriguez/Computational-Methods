%{
#include "y.tab.h"
%}

%%


"a"|"the"                return ARTICLE; 


"boy"|"girl"|"flower"     return NOUN; 


"touches"|"likes"|"sees"   return VERB; 


"with"                 return PREPOSITION; 


[\t] ;              
\n ;                 return EOL; 
.                   return yytext[0]; 

%%