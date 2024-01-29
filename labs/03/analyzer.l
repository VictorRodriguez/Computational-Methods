%{
#include "y.tab.h"
%}

%{
int spacing = 1;
%}

%%
a | 
the         		{ return ARTICLE; }

boy | 
girl | 
flower      		{ return NOUN; }

touches | 
likes | 
sees        		{ return VERB; }

with        		{ return PREP; }

[ \t]+                   /* ignore whitespace */
^[ \t]*\n                /* ignore blank lines */

\n                       { spacing++; return '\n'; }

%%
