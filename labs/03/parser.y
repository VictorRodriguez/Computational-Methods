%{
#include <stdio.h>
%}

%token ARTICLE NOUN VERB PREPOS ENDLINE 

%%
sentence : noun_phrase verb_phrase ENDLINE               {printf("PASS\n");}
         | noun_phrase verb_phrase prep_phrase ENDLINE   {printf("PASS\n");}
         ;

noun_phrase : cmplx_noun                         { }
            | cmplx_noun prep_phrase             { }
            ;

verb_phrase : cmplx_verb                         { }
            | cmplx_verb prep_phrase             { }
            ;

prep_phrase : PREPOS cmplx_noun                  { }
            ;

cmplx_noun : ARTICLE NOUN                        { }
           ;

cmplx_verb : VERB                                { }
           | VERB noun_phrase                    { }
           ;
%%
