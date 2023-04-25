%{
#include "y.tab.h"
%}

%%

a	{ return ARTICLE; }
the	{ return ARTICLE; }

boy	{ return NOUN; }
girl	{ return NOUN; }
flower	{ return NOUN; }

touches { return VERB; }
likes	{ return VERB; }
sees	{ return VERB;}
with	{ return PREP; }
[\t];
[\n]	{ return EOL; }
.	{}
%%
