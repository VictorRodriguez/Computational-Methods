%{
#include <stdio.h>
#include "y.tab.h"
%}
%%
a|the	{ yylval.sval = strdup(yytext); return ARTICLE; }
boy|girl|flower	{ yylval.sval = strdup(yytext); return NOUN; }
touches|likes|sees	{ yylval.sval = strdup(yytext); return VERB; }
with	{ return PREP; }
[ \t] ; 		
\n { return 0; };	
%%

int main(int argc, char **argv) {
    FILE    *fd;

    if (argc == 2)
    {
        if (!(fd = fopen(argv[1], "r")))
        {
            perror("Error: ");
            return (-1);
        }

        yyin = fd;
        
        
        char ch;
    int lines = 0;
         // Counting the total number of lines in the file
        while ((ch = fgetc(fd)) != EOF) {
            if (ch == '\n') {
                lines++;
            }
        }
        
        fseek(fd, 0, SEEK_SET);
	for(int i=0;i<lines;i++)
	yyparse();
        

        fclose(fd);

        
    }
    else
        printf("Usage: a.out filename\n");
    return (0);
}



