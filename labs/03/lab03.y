%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern FILE *yyin;
extern int yylineno;

void yyerror(const char *s) {
    fprintf(stderr, "Error en la línea %d: %s\n", yylineno, s);
}
%}

%token A THE BOY GIRL FLOWER TOUCHES LIKES SEES WITH

%start sentence

%%

// ⟨SENTENCE⟩ → ⟨NOUN-PHRASE⟩⟨VERB-PHRASE⟩ 
sentence: noun_phrase verb_phrase { printf("PASS\n"); }
;

// ⟨NOUN-PHRASE⟩ → ⟨CMPLX-NOUN⟩ | ⟨CMPLX-NOUN⟩⟨PREP-PHRASE⟩
noun_phrase: cmplx_noun
           | cmplx_noun prep_phrase
;

// ⟨VERB-PHRASE⟩ → ⟨CMPLX-VERB⟩ | ⟨CMPLX-VERB⟩⟨PREP-PHRASE⟩
verb_phrase: cmplx_verb
           | cmplx_verb prep_phrase
;

// ⟨PREP-PHRASE⟩ → ⟨PREP⟩⟨CMPLX-NOUN⟩
prep_phrase: prep cmplx_noun
;

// ⟨CMPLX-NOUN⟩ → ⟨ARTICLE⟩⟨NOUN⟩
cmplx_noun: article noun
;

// ⟨CMPLX-VERB⟩ → ⟨VERB⟩ | ⟨VERB⟩⟨NOUN-PHRASE⟩
cmplx_verb: verb
          | verb noun_phrase
;

// ⟨ARTICLE⟩ → a | the
article: A
       | THE
;

// ⟨NOUN⟩ → boy | girl | flower
noun: BOY
    | GIRL
    | FLOWER
;

// ⟨VERB⟩ → touches | likes | sees
verb: TOUCHES
    | LIKES
    | SEES
;

// ⟨PREP⟩ → with
prep: WITH
;

%%

int main(int argc, char **argv) {
    if (argc == 2) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error al abrir el archivo: ");
            return 1;
        }

        yyparse();
        fclose(yyin);

    } else {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        return 1;
    }

    return 0;
}
