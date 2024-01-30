%{
#include "y.tab.h"
#include <stdio.h>

int line_number = 1;
%}

%%

"a"                  { return A; }
"the"                { return THE; }
"boy"                { return BOY; }
"girl"               { return GIRL; }
"flower"             { return FLOWER; }
"touches"            { return TOUCHES; }
"likes"              { return LIKES; }
"sees"               { return SEES; }
"with"               { return WITH; }
[ \t]+               ; /* Ignora espacios en blanco */
\n                   { line_number++; /* Retorno de carro opcional */ }

%%

int yywrap(void) {
    return 1;
}

