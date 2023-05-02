%{
#include "y.tab.h"
%}

%%

a|the               {return ARTICLE;}
boy|girl|flower     {return NOUN;}
touches|likes|sees  {return VERB;}
with                {return PREP;}
\n                  {return EOL;} 
[ \t]+    { /* ignore whitespace */ }

		
.                 { return *yytext; }

%%
