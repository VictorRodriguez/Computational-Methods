%{
 #include <stdio.h>
 int yylex();
 void yyerror(const char *s);
 extern FILE *yyin;
 %}

 %token ARTICLE NOUN VERB PREP EOL

 %%

 sentences: sentence { printf("PASS\n");}
 	| sentences EOL sentences
  | sentences EOL
 	;

 sentence: noun_phrase verb_phrase

 noun_phrase: cmplx_noun | cmplx_noun prep_phrase;

 verb_phrase: cmplx_verb | cmplx_verb prep_phrase;

 prep_phrase: PREP cmplx_noun;

 cmplx_noun: ARTICLE NOUN;

 cmplx_verb: VERB | VERB noun_phrase;

 %%

 void yyerror(const char *s){
 	printf("FAIL\n");
 }

 int main(int argc, char* *argv){

 	FILE *input = fopen(argv[1],"r");

 	if(!input){
 		printf("Error opening file\n");
 		return 1;
 	}
 	yyin=input;
 	yyparse();
 	fclose(input);

 	return 0;

 }
