%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Declaraciones de funciones
extern int yylex();
extern int yyerror(char *msg);

int position_x = 0;  
int position_y = 0;

void move_robot(int num_blocks, int num_degrees);

%}

// Definición de tokens como enumeraciones
%token ROBOT PLEASE MOVE BLOCKS AHEAD AND THEN TURN DEGREES COMMA NUM_BLOCKS NUM_DEGREES

%%

program: orders
       ;

orders: ROBOT PLEASE order
      | orders order
      ;

order:   order COMMA THEN action
		|order COMMA action
		|order AND THEN action
		|order AND action
		|action
       ;

action: MOVE NUM_BLOCKS BLOCKS AHEAD
		{
			move_robot($2, 0);
		}
		|MOVE NUM_BLOCKS BLOCKS
		{
			move_robot($2, 0);
		}
		
		|TURN NUM_DEGREES DEGREES
		{
			move_robot(0, $2);
		}
		
      ;

%%

void move_robot(int num_blocks, int num_degrees) {

    position_x += num_blocks * cos(num_degrees * M_PI / 180.0);
    position_y += num_blocks * sin(num_degrees * M_PI / 180.0);


    if (position_x < 0 || position_x >= 10 || position_y < 0 || position_y >= 10) {
        fprintf(stderr, "Error: Illegal instruction - out of bounds.\n");
        exit(EXIT_FAILURE);
    }
	
	printf("Robot is now at position (%d, %d).\n", position_x, position_y);
}

int yywrap() {
    // Return 1 to indicate the end of input (no more files to process)
    return 1;
}


int yyerror(char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
    exit(EXIT_FAILURE);
}

int main() {
    yyparse();  // Call the parser function
    return 0;
}