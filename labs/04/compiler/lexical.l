%{
#include "y.tab.h"
extern int yylval;

%}

%%


Robot	            { return NOUN; }

please	            {  return KWORD;}

move	            {  return MOVE;}

turn                {  return TURN;}

90 |
180 |
270 |
360                 { yylval = atoi (yytext); return DEGREES_NUM; }

[0-9]+              {  yylval = atoi (yytext); return NUMBER;}

block[s]?           { return BLOCKS;}

degree[s]?[,]?      {  return DEGREES;}

(and[ ])?then |
and                 { return JUNCTION;}

ahead[,]?           {  return DIRECTION;}



[a-z]+ ;
[ \t]  ;	    /* ignore whitespace */
\n     ;

. return yytext[0];

%%
