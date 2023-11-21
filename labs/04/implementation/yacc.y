%{
#include <stdio.h>
#include <stdbool.h>
int yylex();
void yyerror(const char *s);
void printInstruction(const char* action, int value);

enum Direction {
    LEFT,
    RIGHT,
    UP,
    DOWN
};

typedef struct {
    int x;
    int y;
    enum Direction direction;
} Position;

Position position = {0, 0, RIGHT};

bool isMoveValid(int value);
void move(int value);
void turn(int value);
%}

%token BLOCK_NUMBER DEGREE_NUMBER ROBOT_PLEASE MOVE TURN BLOCKS DEGREES AHEAD THEN NEWLINE

%%

program : statements
        | /* empty */
        ;

statements : statement
           | statement statements
           ;

statement : ROBOT_PLEASE actions NEWLINE
 ;

actions : action
        | action THEN actions
    ;

action : move
       | turn
       ;

move : MOVE BLOCK_NUMBER BLOCKS      {move($2);}
     | MOVE BLOCK_NUMBER BLOCKS AHEAD {move($2);}
     ;

turn : TURN DEGREE_NUMBER DEGREES {turn($2);}
     ;
%%

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}

void printInstruction(const char* action, int value) {
    printf("%s,%d\n", action, value);
}

bool isMoveValid(int value) {
    switch (position.direction) {
        case LEFT:
            return position.x - value >= 0;
        case RIGHT:
            return position.x + value < 10;
        case UP:
            return position.y + value < 10;
        case DOWN:
            return position.y - value >= 0;
    }
}

void move(int value) {
    if (isMoveValid(value)) {
        switch (position.direction) {
            case LEFT:
                position.x -= value;
                break;
            case RIGHT:
                position.x += value;
                break;
            case UP:
                position.y += value;
                break;
            case DOWN:
                position.y -= value;
                break;
        }
        printInstruction("MOV", value);
    } else {
        fprintf(stderr, "Error: Invalid move\n");
    }
}

void turn(int value) {
    switch (value) {
        case 90:
            switch (position.direction) {
                case LEFT:
                    position.direction = DOWN;
                    break;
                case RIGHT:
                    position.direction = UP;
                    break;
                case UP:
                    position.direction = LEFT;
                    break;
                case DOWN:
                    position.direction = RIGHT;
                    break;
            }
            printInstruction("TURN", value);
            break;
        case 180:
            switch (position.direction) {
                case LEFT:
                    position.direction = RIGHT;
                    break;
                case RIGHT:
                    position.direction = LEFT;
                    break;
                case UP:
                    position.direction = DOWN;
                    break;
                case DOWN:
                    position.direction = UP;
                    break;
            }
            printInstruction("TURN", value);
            break;
        case 270:
            switch (position.direction) {
                case LEFT:
                    position.direction = UP;
                    break;
                case RIGHT:
                    position.direction = DOWN;
                    break;
                case UP:
                    position.direction = RIGHT;
                    break;
                case DOWN:
                    position.direction = LEFT;
                    break;
            }
            printInstruction("TURN", value);
            break;
        case 360:
            printInstruction("TURN", value);
            break;
        default:
            fprintf(stderr, "Error: Invalid turn\n");
    }
}

int main() {
    yyparse();
    return 0;
}
