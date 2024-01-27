%{
#include "y.tab.h"
extern int yylval;
%}
%%
"boy"|"girl"|"flower"		{ yylval = yytext[0]; return NOUN;}
"a"|"the"			{ yylval = yytext[0]; return ARTICLE;}
"touches"|"likes"|"sees"	{ yylval = yytext[0]; return VERB;}
"with"				{ yylval = yytext[0]; return PREP;}
[\t];				/* ignore whitespace*/
\n return 0;			/*Logical EOF*/
. return yytext[0];
%%

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE* inputFile = fopen(argv[1], "r");
    if (!inputFile) {
        perror("Error opening file");
        return 1;
    }

    yyin = inputFile;
    yylex();

    fclose(inputFile);
    return 0;
}
