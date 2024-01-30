%{
#include "y.tab.h"
%}

%%
"a"             { return ARTICLE; }
"the"           { return ARTICLE; }
"boy"|"girl"|"flower" { return NOUN; }
"touches"|"likes"|"sees" { return VERB; }
"with"          { return PREP; }
\n              { return 0; }  /* End of input */
[ \t]           ;  /* Skip whitespace */

.               { printf("Invalid token: %s\n", yytext); }

%%

int yywrap() {
    return 1;  /* Indicate end of input */
}

