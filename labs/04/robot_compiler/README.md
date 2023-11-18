# ITESM Robot Language Compiler
Daniel Flores Rodríguez - A01734184

## Explicación

Las reglas para el lenguaje son sencillas, estas consisten en darle instrucciones al un robot,  en este caso el robot se le conoce como "Awesomo".

Estas instrucciones se tienen que solicitar de manera amable, iniciando por las palabras "Awesomo please" seguido del conjunto de instrucciones que se desean que Awesomo lleve a cabo.

Las unicas indicaciones aceptadas por Awesomo son:

- 'move', seguido del numero de bloques que se quieren recorrer
- 'turn', seguido de la magnitud del angulo { angulos aceptados: 90,180,270,360 }

Algunos ejemplos de oraciones:

Validas:
- Awesomo please move 6 blocks ahead, and then turn 270 degrees
- Awesomo please turn 270 degrees, move 5 blocks ahead and finally move 3 blocks ahead
- Awesomo please turn 270 degrees, move 10 blocks, then turn 90 degrees and move 8 blocks


No validas:

- Awesomo move 10 blocks
- Turn 180 degrees, and then move 1 block ahead
- Awesomo please moves 100 blocks ahead
- Awesomo move quickly

Cabe mencionar que el espacio o superficie en donde se puede mover Awesomo mide 10 unidades x 10 unidades y si alguna instrucción conduce a que Awesomo salga del espacio, la instruccion no se aceptará y awesomo la omitirá por el contrario, si las instrucciones son validas, las instrucciones se reflejaran en el archivo ./instructions.asm 

Awesomo inicia en el punto (1, 1) del espacion en donde se encuentra, esto quiere decir que se ubica en la parte superior izquierda, con direccion en 0 grados, con lo cual nos referimos claramente al Este
 
 ## Ejecución del programa

 Para ejecutar el compilador, en la raiz del proyecto ejecute el siguiente comando:
````
$ make
````
*Nota: En caso de no funcionar, ejecute los siguientes comandos:

````
$ yacc -d robot_yacc.y
$ lex robot_lex.l
% gcc y.tab.c lex.yy.c -ly -ll -o robot_compiler
````

Posterior a eso, lo unico que se tiene que hacer es ejecutar el compilador generado llamado "robot_compiler" seguido del documento de entrada. Ejemplo:
````
$ ./robot_compiler ./examples/correct_test.ac
````

Los resultados se veran reflejados en un archivo que se creará despues de ejecutar el compilador y se encontrará en la raiz de la carpeta del proyecto.


En la carpeta de ejemplos se muestran varios ejemplos con los que se pueden probar este compilador, y lo unico que se tiene que hacer es cambiar el nombre del archivo a probar en el comando anterior.

Para despejar el area de trabajo, solo ejecute el siguiente comando:
````
$ make clean
````

posteriormente si lo desea, vuelva a ejecutar el proyecto con el comando 'make'.