%{
#include "y.tab.h"
%}
%%
90|180|270|360          		{ yylval.dval = atoi(yytext); return DEGREES; }
[0-9]+				    		{ yylval.dval = atoi(yytext); return BLOCKS; }
blocks\ ahead|blocks			{ yylval.sval = strdup(yytext); return MNOUN; }
degrees							{ yylval.sval = strdup(yytext); return TNOUN; }
and\ then|,\ then				{ yylval.sval = strdup(yytext); return CONNECTOR; }
Robot                   		{ yylval.sval = strdup(yytext); return ROBOT; }
please|pretty\ please|porfis	{ yylval.sval = strdup(yytext); return KIND; }
move	    	           		{ yylval.sval = strdup(yytext); return MVERB; }
turn    	    	       		{ yylval.sval = strdup(yytext); return TVERB; }
\n return 0;
[ \t] ;
.								{yylval.sval = strdup(yytext); return ERROR; }
%%