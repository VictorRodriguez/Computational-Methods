%{
#include <stdio.h>
#include <stdlib.h>

extern FILE* yyin;
extern FILE* yyout;
extern int yylex();
extern int yyparse();
extern void yyerror(const char* s);

%}

%union {
    int num;
}

%token ROBOT PLEASE MOVE AHEAD AND THEN TURN NUMBER BLOCKS DEGREES
%left '+' '-'
%left '*' '/'
%right UMINUS

%start program

%%

program : instruction
        | program instruction
        ;

instruction : ROBOT PLEASE action_list
            ;

action_list : action
            | action_list action
            ;

action : MOVE NUMBER BLOCKS
       | TURN NUMBER DEGREES
       ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
    exit(1);
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: %s input_file output_file\n", argv[0]);
        return 1;
    }

    FILE* inputFile = fopen(argv[1], "r");
    if (inputFile == NULL) {
        printf("Error opening input file.\n");
        return 1;
    }

    FILE* outputFile = fopen(argv[2], "w");
    if (outputFile == NULL) {
        printf("Error opening output file.\n");
        fclose(inputFile);
        return 1;
    }

    yyin = inputFile;
    yyout = outputFile;
    yyparse();

    fclose(inputFile);
    fclose(outputFile);
    return 0;
}

