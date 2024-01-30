/* 	
	STUDENT INFORMATION
	
	Rodrigo López Guerra
	A01737437

	Laboratorio 3.

	Lexical Analyzer Program
*/

/* 	DEFINICIONES     */ 

%{
#include "y.tab.h"
%}

/* 	OPCIONES     */ 

%option noyywrap

/* 	REGLAS Y TOKENS     */ 

%%

"a"|"the"	{ return ARTICLE; }

"boy"|"girl"	{ return NOUN; }

"flower"	{ return GNOUN; }

"touches"|"likes"|"sees"	{ return VERB; }

"with"		{ return PREP; }

\n          { return EOL; } 

[ \t]+    { /* Ignora espacios en blanco */ }

%%