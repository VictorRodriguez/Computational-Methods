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

[aA] | 
[tT]he	{ return ARTICLE; }

[bB]oy | 
[gG]irl	{ return NOUN; }

[fF]lower	{ return GNOUN; }

[tT]ouches |
[lL]ikes | 
[sS]ees	{ return VERB; }

[wW]ith		{ return PREP; }

\n          { return EOL; } 

[ \t]+    { /* Ignora espacios en blanco */ }

%%