%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
FILE *asmFile;

%}


%token NOUN KWORD MOVE TURN DEGREES DEGREES_NUM NUMBER BLOCKS JUNCTION DIRECTION
%%

input : 
 | input sentence 
 ;

sentence: NOUN KWORD action_phrase                  {printf("--------PASS--------\n");}
 ;

action_phrase : action_cmd 
| action_cmd junction_phrase

action_cmd : maction
| taction  


junction_phrase: JUNCTION action_phrase
;

maction : MOVE NUMBER BLOCKS DIRECTION              {fprintf(asmFile, "MOV, %d\n", $2); printf("MOV, %d\n", $2);}
| MOVE DEGREES_NUM BLOCKS DIRECTION                     {fprintf(asmFile, "MOV, %d\n", $2); printf("MOV, %d\n", $2);}
;

taction: TURN DEGREES_NUM DEGREES                   {fprintf(asmFile, "TURN, %d\n", $2); printf("TURN, %d\n", $2);}
;

%%

#include <stdio.h>
#include <stdlib.h>

// stuff from lex that yacc needs to know about:
extern int yylex();
extern int yyparse();
extern FILE *yyin;

int main(int argc, char* argv[]){
  // open a file handle to a particular file:
  FILE *myfile = fopen(argv[1], "r");

  asmFile = fopen("instructions.asm", "w");

  // make sure it's valid:
  if (!myfile) {
    printf("Couldnt open the file!");
    return -1;
  }

  if(!asmFile){
    printf("Couldnt open out file!");
    return -1;
  }
  // set lex to read from it instead of defaulting to STDIN:
  yyin = myfile;
  
  // lex through the input:
	do {
		yyparse();
	} while (!feof(yyin));

  fclose(myfile);
}

void yyerror(const char *s) {
    printf("FAIL\n");
}