%{



#include <stdio.h>

#include <stdlib.h>



int yylex(void);

void yyerror(const char *s);

int yywrap(void);



extern FILE *yyin;



%}



%token ARTICLE NOUN VERB PREP



%%



start: sentences '\n' { printf("PASS\n"); }



sentences: /* empty */

          | sentences sentence '\n'

          ;



sentence: noun_phrase verb_phrase { printf("PASS\n"); }

        | noun_phrase { printf("PASS\n"); }

        | verb_phrase { printf("PASS\n"); }

        ;



noun_phrase: ARTICLE NOUN

           | ARTICLE NOUN prep_phrase

           ;



verb_phrase: VERB

           | VERB noun_phrase

           ;



prep_phrase: PREP noun_phrase

           ;



%%



int main(int argc, char *argv[]) {

    if (argc != 2) {

        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);

        return 1;

    }



    FILE *file = fopen(argv[1], "r");

    if (file == NULL) {

        perror("Error opening file");

        return 1;

    }



    yyin = file;  // Set the input file for Flex/Bison



    yyparse();



    fclose(file);



    return 0;

}



void yyerror(const char *s) {

    fprintf(stderr, "%s\n", s);

}

