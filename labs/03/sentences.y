%{
#include <stdio.h>
extern int yylex(void);
extern int yyparse();
int yyerror(char* s);
extern FILE *yyin;
int passed;

%}
%token ARTICLE VERB NOUN PREP EOL
%%

sentences: sentence {printf("PASS\n");}
 | sentences EOL 
 | sentences EOL sentences 
 ;

sentence: NOUNPHRASE VERBPHRASE
;

NOUNPHRASE: CMPLXNOUN
 | CMPLXNOUN PREPPHRASE
 ;  
 
 VERBPHRASE: CMPLXVERB
 | CMPLXVERB PREPPHRASE
 ;  
 
 PREPPHRASE: PREP CMPLXNOUN
 ;
 
 CMPLXNOUN: ARTICLE NOUN
 ;
 
 CMPLXVERB: VERB
 | VERB NOUNPHRASE
 ; 
 
%% 
int main(int argc, char **argv) {
    FILE *fd;
    char c;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyin = fd;
        
        yyparse();
        yylex();
        fclose(fd);
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}
