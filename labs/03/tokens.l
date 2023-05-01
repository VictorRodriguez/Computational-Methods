%{
#include "y.tab.h"
%}

%%
a               { return ARTICLE; }
the             { return ARTICLE; }
boy             { return NOUN; }
girl            { return NOUN; }
flower          { return NOUN; }
touches         { return VERB; }
likes           { return VERB; }
sees            { return VERB; }
with            { return PREP; }
\n              { return EOL; }
[ \t]+          { }
.               { printf("Invalid input\n"); }
[\r\n]          { /* ignore newline */ }
%%

int yywrap() {
    return 1;
}
