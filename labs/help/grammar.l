%{
#include <stdio.h>
#include "y.tab.h"
%}
%%
"boy"|"girl"|"flower"   return NOUN;
"a"|"the"   return ARTICLE;
"touches"|"likes"|"sees"    return VERB;
"with"  return PREP;
\n              /* ignore end of line */;
[ \t]+          /* ignore whitespace */;
%%
