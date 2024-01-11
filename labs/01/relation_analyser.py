import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def extract_elements(relation):
    """Extract all unique elements from the relation."""
    elements = set()
    for a in relation:
        print (a)
    for a, b in relation:
        elements.add(a)
        elements.add(b)
    return elements

def is_reflexive(relation, elements):
    """Check if the relation is reflexive."""
    for e in elements:
        if (e, e) not in relation:
            return False
    return True

def is_symmetric(relation):
    """Check if the relation is symmetric."""
    for a, b in relation:
        if (b, a) not in relation:
            return False
    return True

def is_transitive(relation):
    """Check if the relation is transitive."""
    for a, b in relation:
        for c, d in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

def analyze(relation, elements):
    """
    Analyze the relation for reflexivity, symmetry, and transitivity.
    """
    # Reflexivity, Symmetry, Transitivity checks
    Reflexive = is_reflexive(relation, elements)
    Symmetric = is_symmetric(relation)
    Transitive = is_transitive(relation)

    return Reflexive, Symmetric, Transitive

def plot():
    """
    Generates the digraph of the relation.
    """
    g = graphviz.Digraph('example')
    g.attr(rankdir='LR', node_shape='circle')

    # Adds the edges for each pair in the relation
    for a, b in relation:
        g.edge(str(a), str(b))

    g.render(filename='graph', format='png', cleanup=True)
    return g

def main():
input_relation = {(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)}
    print(input_relation)
    
    elements = extract_elements(input_relation)

    print("Analyzing input relation!")
    Reflexive, Symmetric, Transitive = analyze(input_relation, elements)
    print(f"1. Reflexive: {Reflexive}")
    print(f"2. Symmetric: {Symmetric}")
    print(f"3. Transitive: {Transitive}")

    # Check for equivalence relation
    if Reflexive and Symmetric and Transitive:
        print("(d) R has an equivalence relation.")
    else:
        print("(d) R does not have an equivalence relation.")

    plot(input_relation)

if __name__ == "__main__":
    main()
