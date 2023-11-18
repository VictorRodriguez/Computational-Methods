/* 
Daniel Flores Rdz A01734184
Fecha de modificación: 17 Nov 2023
*/

%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s){
    fprintf(stderr, "%s\n", s);
    fprintf(stdout, "%s\n", s);
}

extern FILE* yyin;
%}


/* Definimos tokens a usar en el analizador */

%union {
 double dval;
}

%token ROBOT PLEASE MOVE TURN
%token <dval> NUMBER

/* 
Declaramos e inicializamos variables de ubicacion de Awesomo,
cabe mencionar que se toma como punto de salida la posicion (0, 0) 
es decir la esquina superior izquierda del espacio y con la direccion
 de Awesomo apuntando al Este (0 grados)
*/
%{
    int currentX = 0;
    int currentY = 0;
    int currentAngle = 0;
%}


/* Declaramos reglas... */
%%

program: 
        | instruction
        ;

instruction: ROBOT PLEASE action_list
          ;

action_list: action_list action
         | action
         ;

action: MOVE NUMBER 
        {
            int distance = $2;
            // dependiendo del angulo, Awesomo se movera de lugar
            switch(currentAngle){
              case 0: // X positiva (Este)
                currentX += distance;
                break;
              case 180: // X negativa (Oeste)
                currentX -= distance;
                break;
              case 90: // Y positiva (Norte)
                currentY -= distance;
                break;
              case 270: // Y negativa (Sur)
                currentY += distance;
                break;
              default:
                printf("Illegal instruction - invalid angle(s)!\n");
                exit(EXIT_FAILURE);
            }

            if (currentX < 0 || currentX >= 10 || currentY < 0 || currentY >= 10) {
                printf("Illegal instruction - Awesomo pose out of bounds!\n");
                exit(EXIT_FAILURE);
            }
            
            printf("MOV,%d \n", distance);
        }
        | TURN NUMBER 
        {
            // calculamos el angulo referenciandonos desde el ultimo angulo guardado
            int angle = $2;
            currentAngle = (currentAngle + angle) % 360;

            printf("TURN,%d \n", angle);
        }
        ;
     
%%

int main(int argc, char **argv) {
    FILE* fd;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }

        // Crear y abrir el archivo para escribir los impresos en consola
        FILE* output_file = fopen("instructions.asm", "w");
        if (!output_file) {
            perror("Error opening file: ");
            return (-1);
        }

        // Se redirige la salida al archivo de instrucciones
        if (freopen("instructions.asm", "w", stdout) == NULL) {
            perror("freopen");
            exit(EXIT_FAILURE);
        }


        yyin = fd;
        yyparse();

        // Cerramos el archivo de la instruccion (input)
        fclose(fd); 
        // Cerrar el archivo de salida (output)
        fclose(output_file);
        
        }
    else
        printf("Try: ./lex_analaizer filename\n");
    return (0);
}