%{
#include <stdio.h>
extern int yylex();
extern int yyparse();
extern FILE *yyin;
void yyerror(const char *s);
FILE *asmFile;
%}


%union{
        int number;
        int degree;
}

%token ROBOT PLEASE AND THEN COMMA MOVE BLOCKS AHEAD TURN DEGREES EOL

%token <number> NUMBER
%token <degree> DEGREE

%%
sentence_list:
             | sentence_list sentence
             ;

sentence: ROBOT action EOL
        | error EOL { fprintf(asmFile, "INVALID INSTRUCTION\n"); yyerrok; }
        ;

action: PLEASE movement conjuction movement conjuction movement
      | PLEASE movement conjuction movement
      | PLEASE movement
      ;

movement: MOVE NUMBER BLOCKS AHEAD              { fprintf(asmFile, "MOV,%d\n", $2); }
        | TURN DEGREE DEGREES                   { fprintf(asmFile, "TURN,%d\n", $2); }
        ;
conjuction: AND THEN
          | COMMA THEN
          ;

%%

int main(int argc, char **argv) {

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        fprintf(stderr, "ERROR, FILE NOT FOUND\n");
        return 1;
        }

        asmFile = fopen("instructions.asm", "w");

        if (!asmFile) {
        fprintf(stderr, "FILE LOADING FAILED\n");
        fclose(file);
        return 1;
        }

    yyin = file;
    yyparse();

    fclose(file);
    fclose(asmFile);
    return 0;
}

void yyerror(const char *s){
}
