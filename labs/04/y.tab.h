/* A Bison parser, made by GNU Bison 3.8.2.  */



/* Bison interface for Yacc-like parsers in C



   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,

   Inc.



   This program is free software: you can redistribute it and/or modify

   it under the terms of the GNU General Public License as published by

   the Free Software Foundation, either version 3 of the License, or

   (at your option) any later version.



   This program is distributed in the hope that it will be useful,

   but WITHOUT ANY WARRANTY; without even the implied warranty of

   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

   GNU General Public License for more details.



   You should have received a copy of the GNU General Public License

   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */



/* As a special exception, you may create a larger work that contains

   part or all of the Bison parser skeleton and distribute that work

   under terms of your choice, so long as that work isn't itself a

   parser generator using the skeleton or a modified version thereof

   as a parser skeleton.  Alternatively, if you modify or redistribute

   the parser skeleton itself, you may (at your option) remove this

   special exception, which will cause the skeleton and the resulting

   Bison output files to be licensed under the GNU General Public

   License without this special exception.



   This special exception was added by the Free Software Foundation in

   version 2.2 of Bison.  */



/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,

   especially those whose name start with YY_ or yy_.  They are

   private implementation details that can be changed or removed.  */



#ifndef YY_YY_Y_TAB_H_INCLUDED

# define YY_YY_Y_TAB_H_INCLUDED

/* Debug traces.  */

#ifndef YYDEBUG

# define YYDEBUG 0

#endif

#if YYDEBUG

extern int yydebug;

#endif



/* Token kinds.  */

#ifndef YYTOKENTYPE

# define YYTOKENTYPE

  enum yytokentype

  {

    YYEMPTY = -2,

    YYEOF = 0,                     /* "end of file"  */

    YYerror = 256,                 /* error  */

    YYUNDEF = 257,                 /* "invalid token"  */

    T_BLOCK_NUMBER = 258,          /* T_BLOCK_NUMBER  */

    T_DEGREE_NUMBER = 259,         /* T_DEGREE_NUMBER  */

    T_ROBOT_PLEASE = 260,          /* T_ROBOT_PLEASE  */

    T_MOVE = 261,                  /* T_MOVE  */

    T_TURN = 262,                  /* T_TURN  */

    T_BLOCKS = 263,                /* T_BLOCKS  */

    T_DEGREES = 264,               /* T_DEGREES  */

    T_AHEAD = 265,                 /* T_AHEAD  */

    T_THEN = 266,                  /* T_THEN  */

    T_NEWLINE = 267,               /* T_NEWLINE  */

    T_OTHER = 268                  /* T_OTHER  */

  };

  typedef enum yytokentype yytoken_kind_t;

#endif

/* Token kinds.  */

#define YYEMPTY -2

#define YYEOF 0

#define YYerror 256

#define YYUNDEF 257

#define T_BLOCK_NUMBER 258

#define T_DEGREE_NUMBER 259

#define T_ROBOT_PLEASE 260

#define T_MOVE 261

#define T_TURN 262

#define T_BLOCKS 263

#define T_DEGREES 264

#define T_AHEAD 265

#define T_THEN 266

#define T_NEWLINE 267

#define T_OTHER 268



/* Value type.  */

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

typedef int YYSTYPE;

# define YYSTYPE_IS_TRIVIAL 1

# define YYSTYPE_IS_DECLARED 1

#endif





extern YYSTYPE yylval;





int yyparse (void);





#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
