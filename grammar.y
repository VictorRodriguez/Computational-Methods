//A01781041
%{
#include <stdio.h>
#include <stdlib.h>

// Declare yyin and yylineno if they're not already defined by Flex
extern FILE *yyin;
extern int yylineno;

void yyerror(const char *s) {
  fprintf(stderr, "Error: %s at line %d\n", s, yylineno);
  exit(EXIT_FAILURE);
}

int yylex(void);
%}

%token ARTICLE BOY GIRL FLOWER TOUCHES LIKES SEES WITH

%%

SENTENCE: NOUN_PHRASE VERB_PHRASE
        ;

NOUN_PHRASE: ARTICLE NOUN
           | ARTICLE NOUN PREP_PHRASE
           ;

NOUN: BOY
    | GIRL
    | FLOWER
    ;

VERB_PHRASE: VERB
           | VERB NOUN_PHRASE
           ;

VERB: TOUCHES
    | LIKES
    | SEES
    ;

PREP_PHRASE: WITH NOUN_PHRASE
           ;

%%

int main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  FILE *file = fopen(argv[1], "r");
  if (!file) {
    perror(argv[1]);
    exit(EXIT_FAILURE);
  }

  yyin = file;

  // Parse through the input until there is no more:
  do {
    yyparse();
  } while (!feof(yyin));

  fclose(file);
  return 0;
}
