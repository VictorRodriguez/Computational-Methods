%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
extern FILE* yyin;
FILE* output;
%}

%union {
 int dval;
 char *sval;
 }


%token <dval> DEGREES
%token <dval> BLOCKS
%token <sval> TNOUN
%token <sval> MNOUN
%token <sval> ROBOT
%token <sval> KIND
%token <sval> TVERB
%token <sval> MVERB
%token <sval> CONNECTOR
%token <sval> ERROR

%type <sval> actions
%%



statement: ROBOT KIND actions
| ERROR	{printf("Lexical error: %s\n",$1); fclose(yyin); fclose(output); return 0; /*In case there's an error we stop everything and return the Lexical error*/}
;
actions: action
| action CONNECTOR actions
;
action: MVERB BLOCKS MNOUN {fprintf(output,"mov,%d\n",$2);}
| TVERB DEGREES TNOUN {fprintf(output,"turn,%d\n",$2);}
;
%%

int main(int argc, char **argv) {
    FILE    *fd;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyin = fd;
        output = fopen("instructions.asm","w");
        yyparse();
        fclose(fd);
		fclose(output);
    }
    else
        printf("Usage: ./lex_analaizer filename\n");
    return (0);
}