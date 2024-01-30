%{
#include "y.tab.h"
%}

%%

"a"                     { return ARTICLE; }
"the"                   { return ARTICLE; }
"boy"|"girl"|"flower"   { return NOUN; }
"touches"|"likes"|"sees" { return VERB; }
"with"                  { return PREP; }
\n                      { return EOL; }
.                       { /* ignore anything else */ }

%%

int yywrap() {
    return 1;
}

