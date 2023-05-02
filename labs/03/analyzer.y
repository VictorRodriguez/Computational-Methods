%{ 

#include <stdio.h>

int yylex(void);
int yyparse(void);
int yy_scan_string(char *);
void yyerror(char *);

extern FILE *yyin;

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

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("[!] Insufficient arguments!\n");
        printf("[!] Correct ussage: ./analyzer test.txt\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");

    if (input == NULL)
    {
        printf("[!] Error opening file: %s\n", argv[1]);
        return 1;
    }
    
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, input)) != -1)
    {
        if (line[read - 1] != '\n')
        {
            strncat(line, "\n", 1);
        }
        yy_scan_string(line);
        yyparse();
    }
    
    free(line);
    fclose(input);
}

void yyerror(char *s)
{
    printf("FAIL\n");
}
