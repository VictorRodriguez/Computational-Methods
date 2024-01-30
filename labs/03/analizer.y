%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%union {
 char *sval;
 }

%token <sval> ARTICLE NOUN VERB PREP
%type <sval> nounphrase verbphrase prepphrase complexnoun complexverb sentence


%%

input: sentence	{printf("PASS\n");}
 ;
sentence: nounphrase verbphrase
 ;
nounphrase: complexnoun	
	| complexnoun prepphrase        
 ; 
verbphrase: complexverb
 ;
prepphrase: PREP complexnoun	    
 ;
complexnoun: ARTICLE NOUN	    
 ;
complexverb: VERB
	| VERB nounphrase    
 ;
 
%%
 

