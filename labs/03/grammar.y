%{
#include <stdio.h>

int yylex();
void yyerror(const char *s);

#define PASS 1
#define FAIL 0

extern FILE* yyin;

%}

%token ARTICLE NOUN VERB PREP EOL

%%

sentence_list: sentence EOL        { if ($1 == PASS) printf("PASS\n"); else printf("FAIL\n"); }
             | sentence_list sentence EOL { if ($2 == PASS) printf("PASS\n"); else printf("FAIL\n"); }
             ;

sentence: noun_phrase verb_phrase    { $$ = $1 && $2; }
        ;

noun_phrase: cmplx_noun              { $$ = $1; }
           | cmplx_noun prep_phrase  { $$ = $1 && $2; }
           ;

verb_phrase: cmplx_verb              { $$ = $1; }
           | cmplx_verb prep_phrase  { $$ = $1 && $2; }
           ;

prep_phrase: PREP cmplx_noun         { $$ = $2; }
           ;

cmplx_noun: ARTICLE NOUN             { $$ = PASS; }
          ;

cmplx_verb: VERB                     { $$ = PASS; }
          | VERB noun_phrase         { $$ = $2; }
          ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening file");
        return 1;
    }

    yyin = input_file;
    yyparse();
    fclose(input_file);

    return 0;
}

