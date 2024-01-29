%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%token PREP ARTICLE NOUN VERB
%start sentence

%%

/*
A = noun-phrase
B = verb phrase
C = Prep Phrase
D = complx noun
E = cmplx verb
F = Article
G = Noun
H = Verb
I = Prep
*/

sentence : AB { printf("PASS\n"); }
         | { printf("FAIL\n"); }
         ;

AB : A B
   ;

A : D
  | D C
  ;

B : E
  | E C
  ;

D : F G
  ;

C : I D
  ;

E : H
  | H A
  ;

I : "with"
  ;

F : "a"
  | "the"
  ;

G : "boy"
  | "girl"
  | "flower"
  ;

H : "touches"
  | "likes"
  | "sees"
  ;

%%

int main() {
    yyparse();
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
