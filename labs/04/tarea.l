%{
#define NUMBER 400
#define COMMENT 401
#define TEXT 402
#define COMMAND 403
%}

%%

[ \t]+                              
[0-9]+                              { return NUMBER; }
[0-9]+\.[0-9]+                      { return NUMBER; }
\.[0-9]+                            { return NUMBER; }
"#[^\\n]*"                          { return COMMENT; }
"\"[^\"]*\""                        { return TEXT; }
[a-zA-Z][a-zA-Z0-9]*                { return COMMAND; }
\n                                  

%%

#include <stdio.h>

int main(int argc, char **argv) {
    int val;
    while((val = yylex())) {
        printf("Token: %d\n", val);
    }
    return 0;
}

