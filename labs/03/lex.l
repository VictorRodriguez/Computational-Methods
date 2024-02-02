%{
#include "y.tab.h"
%}

%%

 "the" | "a"                     { return ARTICLE; }

 "boy" | "girl" | "flower"       { return NOUN; }

 "touches" | "likes" | "sees"    { return VERB; }

 "with"                          { return PREP; }

 \n                              { return '\n'; }

 .                               { return yytext[0]; }

%%

int yywrap() {

    return 1;

}
