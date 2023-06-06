%{
#include <stdio.h>
extern int yylex();
extern FILE *yyin;
void yyerror(const char *s);
%}

%token  NOUN KIND VERB INUM UNITS DIRECTION ADVERB CONJUNCTION EOL
%start	CMD_SENTENCE

%%
CMD_SENTENCE:	
     		|SENTENCE;

SENTENCE: 	NOUN KIND COMMAND  {printf("CORRECT COMMAND\n");} 
		| error EOL {printf("FAIL\n"); yyerror; }

COMMAND: 	STRAIGHT_CMD	// "move..."
		|TURN_CMD	// "turn..."
		|PHRASE_CMD
		
STRAIGHT_CMD:	VERB INUM UNITS DIRECTION	// "move 5 blocks ahead"

TURN_CMD:	VERB INUM UNITS 		// "turn 180 degrees"

PHRASE_CMD:	CONJUNCTION STRAIGHT_CMD // "and move..."
		|CONJUNCTION TURN_CMD	// "and turn..."
		|CONJUNCTION ADVERB STRAIGHT_CMD	// "and then move..."
		|CONJUNCTION ADVERB TURN_CMD	// "and then turn..."
%%

int main(int argc, char* argv[]) {

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        fprintf(stderr, "ERROR, FILE NOT FOUND ...\n");
        return 1;
    }

    yyin = file;
    yyparse();
    fclose(file);

    return 0;
}

void yyerror(const char *s){
	printf("FAAAIL\n");
}
