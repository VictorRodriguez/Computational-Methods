Lo hice en windows, así que no creo que mi makefile le ayude mucho, pero en powershell lo compilo así:

flex lex.l

bison -yd yacc.y

gcc -o ola y.tab.c lex.yy.c -L "C:\Gnuwin32\lib" -lfl

por alguna razón gcc no puede encontrar en linker solito así que hay que ponerle el link :)
