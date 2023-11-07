# Lex code

%%

%option noyywrap

word = [a-zA-Z]+
number = [0-9]+

%%

{word} {
  printf("MOV, %s\n", yytext);
}

{number} {
  printf("TURN, %d\n", atoi(yytext));
}

\n {
  // Ignore newlines
}

. {
  // Error
  printf("Error: unexpected character '%c'\n", yytext[0]);
}

%%

# Yacc grammar

grammar robot;

options {
  output = "robot.c";
}

tokens {
  MOV;
  TURN;
}

start = sentence;

sentence = 
    polite_word "move" number "blocks" {printf("MOV, %d\n", $3);}
  | polite_word "turn" number "degrees" {printf("TURN, %d\n", $3);}
  | sentence polite_word "and" sentence;

polite_word =
    "please";

%%
