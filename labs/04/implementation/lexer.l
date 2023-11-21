%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
[1-9]                               {yylval = atoi(yytext); return BLOCK_NUMBER;}
90|180|270|360                      {yylval = atoi(yytext); return DEGREE_NUMBER;}
Robot[ ]please                      {return ROBOT_PLEASE;}
move                                {return MOVE;}
turn                                {return TURN;}
degrees                             {return DEGREES;}
blocks|block                        {return BLOCKS;}
ahead                               {return AHEAD;}
(and|,)?[ ]then                     {return THEN;}
(\n|\r\n|\r)                        {return NEWLINE;}
[\t \s]                             ;
.                                   {return yytext[0];}
%%