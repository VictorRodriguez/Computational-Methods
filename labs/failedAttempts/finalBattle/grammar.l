%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"  // Include the correct path to y.tab.h

extern int yyparse(void);
extern void checkIfSuccessful(void);
%}

%%
a       { return ARTICLE; }
the     { return ARTICLE; }
boy     { return NOUN; }
girl    { return NOUN; }
flower  { return NOUN; }
touches { return VERB; }
likes   { return VERB; }
sees    { return VERB; }
with    { return PREP; }
\n      { return EOL; }
.       { return yytext[0]; } // Match any other character
%%

int main(int argc, char **argv) {
    FILE *fd;

    if (argc == 2) {
        if (!(fd = fopen(argv[1], "r"))) {
            perror("Error: ");
            return (-1);
        }

        yyset_in(fd);

        // Reset state variables
        yyparse();

        fclose(fd);

        // Call checkIfSuccessful after parsing
        checkIfSuccessful();
    } else {
        printf("Usage: a.out filename\n");
    }

    return (0);
}

