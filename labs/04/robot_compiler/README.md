# Compilador de Lenguaje para Robot ITESM

## Autor
Daniel Flores Rodríguez - A01734184

## Descripción General

El Compilador de Lenguaje para Robot ITESM facilita la comunicación con un robot llamado "Awesomo" al proporcionar un lenguaje sencillo para emitir instrucciones. Las reglas del lenguaje son simples: las instrucciones deben ser educadas y comenzar con la frase "Awesomo please," seguida del conjunto deseado de acciones.

Las instrucciones aceptadas para Awesomo son:

- 'move', seguido del número de bloques a recorrer.
- 'turn', seguido de la magnitud del ángulo {ángulos aceptados: 90, 180, 270, 360}.

### Ejemplos:

#### Válidos:
- Awesomo please move 6 blocks ahead, and then turn 270 degrees
- Awesomo please turn 270 degrees, move 5 blocks ahead and finally move 3 blocks ahead
- Awesomo please turn 270 degrees, move 10 blocks, then turn 90 degrees and move 8 blocks

#### No válidos:
- Awesomo move 10 blocks
- Turn 180 degrees, and then move 1 block ahead
- Awesomo please moves 100 blocks ahead
- Awesomo move quickly

Awesomo opera en un espacio de 10x10 unidades. Si una instrucción lleva a Awesomo fuera de este espacio, la instrucción será rechazada y Awesomo la omitirá. Las instrucciones válidas se reflejarán en el archivo `./instructions.asm`.

Awesomo comienza en el punto (1, 1) en el espacio, denotando la esquina superior izquierda, mirando hacia el Este a 0 grados.

## Ejecución

Para ejecutar el compilador, use el siguiente comando en la raíz del proyecto:
```bash
$ make
```

*Nota: Si esto no funciona, ejecute los siguientes comandos:

````
$ yacc -d robot_yacc.y
$ lex robot_lex.l
% gcc y.tab.c lex.yy.c -ly -ll -o robot_compiler
````

Luego ejecuta el compilador generado, llamado "robot_compiler," seguido del documento de entrada. Ejemplo:
````
$ ./robot_compiler ./examples/correct_test.ac
````

Los resultados se reflejarán en un archivo creado después de ejecutar los comandos anteriores, ubicado en la raíz del proyecto.

La carpeta 'examples' contiene varios casos de prueba. Simplemente cambie el nombre del archivo en el comando anterior para probar diferentes escenarios.

Para limpiar el espacio de trabajo, ejecuta:
````
$ make clean
````

Después, si se desea, vuelva a ejecutar el proyecto con el comando 'make'.
