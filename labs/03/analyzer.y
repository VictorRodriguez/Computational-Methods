%{ 
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP 

%%

start: SENTENCES '\n' { printf("PASS\n"); }


SENTENCES: /* empty */| SENTENCES SENTENCE '\n';

SENTENCE: NOUN_PHRASE VERB_PHRASE { printf("PASS\n"); }
        | NOUN_PHRASE { printf("PASS\n"); }
        | VERB_PHRASE { printf("PASS\n"); }

NOUN_PHRASE: ARTICLE NOUN| ARTICLE NOUN PREP_PHRASE;

VERB_PHRASE: VERB| VERB NOUN_PHRASE;

PREP_PHRASE: PREP NOUN_PHRASE;


%%

void yyerror(const char *s){
	printf("FAIL\n");
}

int main(int argc, char **argv){

    FILE *fd;

     if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }
        yyin=fd;
        yyparse();
        fclose(fd);
    }

	return 0;
}
