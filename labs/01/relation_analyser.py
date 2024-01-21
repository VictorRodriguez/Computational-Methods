import graphviz

def analyze(val):
    elements = set()
    for pair in val:
        elements.add(pair[0])
        elements.add(pair[1])

    Reflexive = all((a, a) in val for a in elements)
    Symmetric = all((b, a) in val for (a, b) in val)
    Transitive = all((a, c) in val for (a, b1) in val for (b2, c) in val if b1 == b2)

    return Reflexive, Symmetric, Transitive

def plot(val):
    g = graphviz.Digraph('G', filename='graph.gv')
    for pair in val:
        g.edge(str(pair[0]), str(pair[1]))
    with open('graph.log', 'w') as f:
        f.write(str(g))

def main():
    print("Analyzing input!")
    val_input = "[(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)]"
    val = eval(val_input)
    print(val)
    Reflexive, Symmetric, Transitive = analyze(val)
    print(f"\
    (a) R is {'reflexive' if Reflexive else 'not reflexive'}, \
    (b) R is {'symmetric' if Symmetric else 'not symmetric'}, \
    (c) R is {'transitive' if Transitive else 'not transitive'}.")
    if Reflexive and Symmetric and Transitive:
        print("(d) R is an equivalence relation.")
    else:
        print("(d) R is not an equivalence relation.")
    plot(val)

if __name__ == "__main__":
    main()

