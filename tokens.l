%{
#include "grammar.tab.h"
%}

%option yylineno

%%

[aA]                     { return ARTICLE; }
boy                      { return BOY; }
girl                     { return GIRL; }
flower                   { return FLOWER; }
touches                  { return TOUCHES; }
likes                    { return LIKES; }
sees                     { return SEES; }
with                     { return WITH; }
[ \t\n]+                 ; /* Ignore whitespaces and newlines */
.                        ; /* Ignore other characters */

%%

int yywrap(void) {
  return 1;
}
