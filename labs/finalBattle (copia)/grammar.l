%{
#include "y.tab.h"
%}

%option noyywrap

%%

a               { printf("Token: ARTICLE 'a'\n"); return ARTICLE; }
the             { printf("Token: ARTICLE 'the'\n"); return ARTICLE; }
boy             { printf("Token: NOUN 'boy'\n"); return NOUN; }
girl            { printf("Token: NOUN 'girl'\n"); return NOUN; }
flower          { printf("Token: NOUN 'flower'\n"); return NOUN; }
touches         { printf("Token: VERB 'touches'\n"); return VERB; }
likes           { printf("Token: VERB 'likes'\n"); return VERB; }
sees            { printf("Token: VERB 'sees'\n"); return VERB; }
with            { printf("Token: PREP 'with'\n"); return PREP; }
\n              { printf("Token: EOL '\\n'\n"); return EOL; }
.               { /* ignorar otros caracteres */ }

%%
