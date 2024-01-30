%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}



%%

a|the                       {return ARTICLE;}
boy|girl|flower             {return NOUN;}
touches|likes|sees          {return VERB;}
with                        {return PREP;}

[ \t]+
<<EOF>>                     { return 0; }  
\n

.

%%