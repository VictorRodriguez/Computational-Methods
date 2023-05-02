%{
#include "y.tab.h"
%}

%%
the { return ARTICLE; }
a { return ARTICLE; }
boy { return NOUN; }
girl { return NOUN; }
flower { return NOUN; }
touches { return VERB; }
likes { return VERB; }
sees { return VERB; }
with { return PREP; }
[ \t]+ {} ; // skip spaces and tabs
\n { return EOL; } // treat newlines as end-of-line tokens
. { printf("Invalid Input\n"); } // return other characters as-is
%%

int yywrap() {
return 1;
}