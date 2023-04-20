# EQUIVALENCE WITH FINITE AUTOMATA

Regular expressions and finite automata are equivalent in their descriptive
power. This fact is surprising because finite automata and regular expressions
superficially appear to be rather different. However, any regular expression
can be converted into a finite automaton that recognizes the language it
describes, and vice versa. Recall that a regular language is one that is
recognized by some finite automaton.

A language is regular if and only if some regular expression describes it.

## Activities

Create a program in python that create the equivalence with finite automata:

Alphabet: {0,1} or {a,b}
Alphaphet symbol: A
Empty stringsymbol : E

Example of Input string : (ab ∪ a)*

We convert the regular expression (ab ∪ a)* to an NFA in a sequence of stages.
We build up from the smallest subexpressions to larger subexpressions until we
have an NFA for the original expression, as shown in the following diagram


Output (does not correspond to (ab ∪ a)*  regex):

```graphviz
digraph finite_state_machine {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	rankdir=LR;
	node [shape = doublecircle]; 0 3 4 8;
	node [shape = circle];
	0 -> 2 [label = "SS(B)"];
	0 -> 1 [label = "SS(S)"];
	1 -> 3 [label = "S($end)"];
	2 -> 6 [label = "SS(b)"];
	2 -> 5 [label = "SS(a)"];
	2 -> 4 [label = "S(A)"];
	5 -> 7 [label = "S(b)"];
	5 -> 5 [label = "S(a)"];
	6 -> 6 [label = "S(b)"];
	6 -> 5 [label = "S(a)"];
	7 -> 8 [label = "S(b)"];
	7 -> 5 [label = "S(a)"];
	8 -> 6 [label = "S(b)"];
	8 -> 5 [label = "S(a)"];
}
```

To be tested in https://dreampuf.github.io/GraphvizOnline/


<img width="768" alt="image" src="https://user-images.githubusercontent.com/327548/225399535-510665a4-45ce-4b3b-ae93-b87980456b98.png">


