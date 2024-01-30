%{
#include "y.tab.h"
%}

%%
"the"|"a"                   {return ARTICLE; }
"boy"|"girl"|"flower"       {return NOUN; }
"touches"|"likes"|"sees"    {return VERB; }
"with"                      {return PREPOS; }
\n                          {return ENDLINE; }
[ \t]                       ; /*Sin espacios vacios*/
%%

int yywrap(void) {
    return 1;
}
