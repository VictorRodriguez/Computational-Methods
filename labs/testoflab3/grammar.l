%{
#include <stdio.h>

#define NOUN 1
#define ARTICLE 2
#define VERB 3
#define PREP 4
%}

%%

"boy"|"girl"|"flower"		{ printf("NOUN"); /*return NOUN;*/ }
"a"|"the"			{ printf("ARTICLE"); /*return ARTICLE;*/ }
"touches"|"likes"|"sees"	{ printf("VERB"); /*return VERB;*/ }
"with"				{ printf("PREP"); /*return PREP;*/ }

.		{ /* Ignore any other characters */ }

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
