import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(R):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = False
    Symmetric = False
    Transitive = False

    tempState = ""

    for states in R:
        # Analyze if it is Reflexive
        if (states[0] == states[1]):
            Reflexive = True

        # Analyze if it is Symmetric
        if (states[0] != states[1] and not Symmetric):
            Symmetric = analizeSymmtric(R, states)

        # Analyze if it is Transitive
        if (states[0] != states[1] and not Transitive):
            Transitive = analizeTransitive(R, states)

    return Reflexive, Symmetric, Transitive


def analizeSymmtric(R, actState):
    for states in R:
        if (actState[1] == states[0] and actState[0] == states[1]):
            return True
    return False


def analizeTransitive(R, actState):
    tmpState = []
    firstState = actState[0]

    for states in R:
        if (actState[1] == states[0] and states[0] != states[1] and states[1] != actState[0]):
            tmpState = [states[0], states[1]]

            for states2 in R:
                if (tmpState and firstState == states2[0] and states2[1] == tmpState[1]):

                    return True
    return False


def plot(R):
    g = graphviz.Digraph('G', filename='hello.gv')

    for states in R:
        g.edge(str(states[0]), str(states[1]))

    g.view()


def main():
    print("Hello World analyzing input!")
    R = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    print(R)
    Reflexive, Symmetric, Transitive = analyze(R)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(R)


if __name__ == "__main__":
    main()
