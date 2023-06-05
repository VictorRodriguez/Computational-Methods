%{
#include "y.tab.h"
%}

%%
robot				{ printf("NOUN"); }
please				{ printf("KIND"); }
move|turn			{ printf("VERB"); }
[0-9]+ 				{ printf("INUM"); }
block|blocks|degrees     	{ printf("UNITS"); }
ahead|right|left|behind		{ printf("DIRECTION"); }
then				{ printf("ADVERB"); }
and				{ printf("CONJUCTION"); }
\/\/[^\n]*                      { printf("COMMENTLINE");/* Ignore single-line comments */ }
\/\([^]|[\r\n]|(\+([^/]|[\r\n]))\+\/ 	{ /* Ignore multi-line comments */ }
[\t]+                           { /* Ignore white spaces */ }

"\n "                           { printf("NEWLINE"); }			
%%

int yywrap(){	
    	return 1;
}
