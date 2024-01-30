%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"

extern int wwlex(); /* Use wwlex instead of yylex */
extern void yyerror(const char* s);

int line_number = 1;

%}

%token ARTICLE NOUN VERB PREP

%type <a> ARTICLE NOUN VERB PREP /* Declare the type of the attribute for each terminal */
%type <a> sentence noun_phrase verb_phrase prep_phrase cmplx_noun cmplx_verb /* Declare the type of the attribute for each non-terminal */

%%
sentence : noun_phrase verb_phrase      { printf("PASS\n"); }
         ;

noun_phrase : cmplx_noun              { }
            | cmplx_noun prep_phrase  { }
            ;

verb_phrase : cmplx_verb              { }
            | cmplx_verb prep_phrase  { }
            ;

prep_phrase : PREP cmplx_noun         { }
            ;

cmplx_noun : ARTICLE NOUN            { }
           ;

cmplx_verb : VERB                    { }
           | VERB noun_phrase        { }
           ;



%%

void yyerror(const char* s) {
    fprintf(stderr, "Error at line %d: %s\n", line_number, s);
}

int main(int argc, char **argv) {
    if (argc == 2) {
        FILE *yyin = fopen(argv[1], "r");
        if (!yyin) {
            fprintf(stderr, "Error opening file: %s\n", strerror(errno));  // File opening error
            return 1;  // Return non-zero, indicates an error
        }

        yyparse();  // Parse the input file
        fclose(yyin);  // Closes the file

    } else {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);  // Display usage information for incorrect command-line arguments
        return 1;  // Return non-zero, indicates an error
    }

    return 0;  // Return 0, successful execution
}