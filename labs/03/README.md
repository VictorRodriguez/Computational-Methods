# CFG implemented in Lex and YACC


Lex and yacc help you write programs that transform structured input. This includes
an enormous range of applications—anything from a simple text search program that
looks for patterns in its input file to a C compiler that transforms a source program into
optimized object code.

One of those applications are the context-free grammars (CFG). CFG are a more
powerful method of describing languages. Such grammars can describe certain
features that have a recursive structure, which makes them useful in a variety
of applications.

## Activities

Create a program in LEX and YACC that analyise the CFG:

```
⟨SENTENCE⟩ → ⟨NOUN-PHRASE⟩⟨VERB-PHRASE⟩ ⟨NOUN-PHRASE⟩ → ⟨CMPLX-NOUN⟩ | ⟨CMPLX-NOUN⟩⟨PREP-PHRASE⟩
⟨VERB-PHRASE⟩ → ⟨CMPLX-VERB⟩ | ⟨CMPLX-VERB⟩⟨PREP-PHRASE⟩ ⟨PREP-PHRASE⟩ → ⟨PREP⟩⟨CMPLX-NOUN⟩
⟨CMPLX-NOUN⟩ → ⟨ARTICLE⟩⟨NOUN⟩ ⟨CMPLX-VERB⟩ → ⟨VERB⟩ | ⟨VERB⟩⟨NOUN-PHRASE⟩
⟨ARTICLE⟩ → a | the
⟨NOUN⟩ → boy | girl | flower
⟨VERB⟩ → touches | likes | sees ⟨PREP⟩ → with
```

Example of Input file :

```

a boy sees
the boy sees a flower
a girl with a flower likes the boy
a flower sees a flower
```


Each of these strings has a derivation in grammar

expected way to test yoru code:

```
./analyzer test.txt
PASS
PASS
PASS
FAIL
```
## Student notes:
For the last test, the program should pass because the sentence could also be constructed using the context free grammar. The sentence "a flower sees a flower" can be constructed using the following derivation:

```
1. a flower sees a flower
2. <ARTICLE> <NOUN> <VERB> <ARTICLE> <NOUN>
3. <CMPLX-NOUN> <VERB> <CMPLX-NOUN>
4. <NOUN-PHRASE> <VERB> <NOUN-PHRASE>
5. <NOUN-PHRASE> <CMPLX-VERB>
6. <NOUN-PHRASE> <VERB-PHRASE>
7. <SENTENCE>
```
