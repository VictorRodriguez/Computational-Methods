%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern int yyerror(char *msg);

int x = 0;
int y = 0;
int current_degree = 0;

void move(int blocks);
void update_degree(int degree);

%}


%token ROBOT PLEASE TURN MOVE DEGREES_NUMBER DEGREES BLOCKS_NUMBER BLOCKS THEN

%%

S: ROBOT PLEASE orders
 ;

orders: orders THEN order
      | order
      ;

order:  TURN DEGREES_NUMBER DEGREES
        {
           update_degree($2);
        }

        | MOVE BLOCKS_NUMBER BLOCKS
        {
            move($2);
        }
        ;
%%

void update_degree(int degree)
{
    current_degree = (current_degree + degree) % 360;

    if (current_degree % 90 != 0)
    {
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("TURN, %i\n", degree);
    }
}

void move(int blocks)
{
    switch(current_degree)
    {
      case 0:
        x += blocks;
        break;
      case 90:
        y -= blocks;
        break;
      case 180:
        x -= blocks;
        break;
      case 270:
        y += blocks;
        break;
    }

    if (x > 10 || x < 0 || y > 10 || y < 0)
    {
        printf("outside grid\n");
        exit(EXIT_FAILURE);
    }
    else
    {
        printf("MOV, %i\n", blocks);
    }
}

int yywrap() {
    return 1;
}


int yyerror(char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
    exit(EXIT_FAILURE);
}

int main() {
    yyparse();
    return 0;
}


