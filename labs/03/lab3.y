%{
#include <stdio.h>
void yyerror(const char* s);
int yylex();
extern FILE *yyin;
%}

%token ARTICLE NOUN VERB PREP

%%

sentence:
    noun_phrase verb_phrase { printf("PASS\n"); }
    ;

noun_phrase:
    cmplx_noun 
    | cmplx_noun prep_phrase 
    ;

verb_phrase:
    cmplx_verb 
    | cmplx_verb prep_phrase 
    ;

prep_phrase:
    PREP cmplx_noun 
    ;

cmplx_noun:
    ARTICLE NOUN 
    | ARTICLE NOUN prep_phrase 
    ;

cmplx_verb:
    VERB 
    | VERB noun_phrase 
    ;

%%

void yyerror(const char* s) {
    printf("FAIL\n");
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Using: %s filename\n", argv[0]);
        return 1;
    }

    FILE* file = fopen(argv[1], "r");
    if (!file) {
        printf("Cant open file %s\n", argv[1]);
        return 1;
    }

    yyin = file;
    yyparse();

    fclose(file);
    return 0;
}
