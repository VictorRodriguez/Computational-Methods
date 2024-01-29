/* Created by Hedguhar Domínguez on 29/01/2024. */
/* Syntactic analyzer for the compiler */


%{

#include <stdio.h>
#include <stdlib.h>

// Lex variables
extern int yylex();

// Function prototypes
int yyerror(char const * s);

%}


/* Terminal symbols */
%token A THE BOY GIRL FLOWER TOUCHES LIKES SEES WITH OTHER
%start sentence


%%

// Grammar rules

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


// Error function
int yyerror(char const * s)
{
    fprintf(stderr, "FAIL\n");
}


void main()
{
    yyparse();
}
