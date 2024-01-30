%{
#include "y.tab.h"
%}

%%

"a"|"the"                { return ARTICLE; }
"boy"|"girl"|"flower"    { return NOUN; }
"touches"|"likes"|"sees" { return VERB; }
"with"                   { return PREPOSITION; }
[\t]+                    ; /* ignore whitespace */
\n                       { return EOL; }
.                        ; /* ignore other characters */

%%

int yywrap(void) {
    return 1;
}

