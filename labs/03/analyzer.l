%{
#include "y.tab.h"
%}
%{
int spacing = 1;
%}

%%
a | the         		{ return ARTICLE; }

boy | girl | flower      		{ return NOUN; }

touches | likes | sees        		{ return VERB; }

with        		{ return PREP; }

\n                       { spacing++; return '\n'; }
[ \t]+                    
^[ \t]*\n                

%%
