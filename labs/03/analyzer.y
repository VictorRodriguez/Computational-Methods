%{ 

#include <stdio.h>

%}

%token ARTICLE NOUN VERB PREP EOL

%%

line : sentence EOL { printf("PASS\n"); }
;

sentence : noun_phrase verb_phrase
;   

noun_phrase : cmplx_noun
| cmplx_noun prep_phrase
;

verb_phrase : cmplx_verb
| cmplx_verb prep_phrase
;

prep_phrase : PREP cmplx_noun
;

cmplx_noun : ARTICLE NOUN
;

cmplx_verb : VERB 
| VERB noun_phrase
;

%%

extern FILE *yyin;

main()
{
    // ./analyze < test.txt
    
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, stdin)) != -1)
    {
        yy_scan_string(line);
        yyparse();
    }
    
    free(line);
}

yyerror(char *s)
{
    printf("FAIL\n");
}
