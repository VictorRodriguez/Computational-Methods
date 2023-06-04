%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern int yylval;
extern FILE* yyin;

void yyerror(const char* message);

void execute_movements(int num) {
    printf("MOV,%d\n", num);
}

void execute_turn(int num) {
    printf("TURN,%d\n", num);
}

%}

%token ROBOT_PLEASE MOVE TURN AHEAD DEGREES AND_THEN COMMA NEWLINE NUMBER AHEADC DEGREESC BLOCKS EOF_TOKEN

%%

program : sentences
        ;

sentences : sentence
          | sentences sentence
          ;

sentence : ROBOT_PLEASE action_list NEWLINE { }
         | ROBOT_PLEASE action_list EOF_TOKEN { }
         ;

action_list : action
            | action_list AND_THEN action
            | action_list COMMA action
            | action_list AHEADC action
            | action_list DEGREESC action
            ;

action : MOVE NUMBER BLOCKS AHEAD { execute_movements($2); }
       | TURN NUMBER DEGREES      { execute_turn($2); }
       | MOVE NUMBER BLOCKS { execute_movements($2); }
       | TURN NUMBER      { execute_turn($2); }
       ;

%%

void yyerror(const char* message) {
    if (feof(yyin)) {

    }else{
        fprintf(stderr, "%s\n", message);
    }
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: %s input_file\n", argv[0]);
        return 1;
    }

    FILE* file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    yyin = file;

    yyparse();

    fclose(file);

    return 0;
}
