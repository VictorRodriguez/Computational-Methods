%{
#include <stdio.h>
%}

%%
[a-zA-Z]+	printf("NOUN: %s\n", yytext);
\b(is|am|are|was|were|be|being|been)\b	printf("VERB: %s\n", yytext);
\b(please|thanks|sorry)\b		printf("KIND WORD: %s\n", yytext);
[0-9]+		printf("NUMBER OF BLOCKS: %s\n", yytext);
[0-9]+(°|º)	printf("DEGREES: %s\n", yytext);
[\t\n ] 	// Ignore whitespace and newline characters
. 		// Ignore any other characters

%%

int main() {
    yylex();
    return 0;
}
