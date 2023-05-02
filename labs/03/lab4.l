%{
#include "y.tab.h"
%}

%%
"a"        { return ARTICLE; }
"the"      { return ARTICLE; }
"boy"      { return NOUN; }
"girl"     { return NOUN; }
"flower"   { return NOUN; }
"touches"  { return VERB; }
"likes"    { return VERB; }
"sees"     { return VERB; }
"with"     { return PREP; }
\n         { return EOL; }
[ \t]+     ; /* Ignorar espacios en blanco y tabuladores */
.          { yylval = yytext[0]; return yytext[0]; }
%%

int yywrap(){
    return 1;
}

