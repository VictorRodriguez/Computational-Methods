import ast
import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html


def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = False
    Symmetric = False
    Transitive = False

    X = {i[0] for i in val}
    X.update({i[1] for i in val})

    # Check if the set is Reflexive
    for i in X:
        if (i, i) in val:
            Reflexive = True
        else:
            Reflexive = False
            break

    # Check if the set is Symmetric
    for i in val:
        if (i[1], i[0]) in val:
            Symmetric = True
        else:
            Symmetric = False
            break

    # Check if the set is Transitive
    for i in val:
        for j in val:
            if i[1] == j[0]:
                if (i[0], j[1]) in val:
                    Transitive = True
                else:
                    Transitive = False
                    break

    return Reflexive, Symmetric, Transitive


def plot(val):
    """
    Here goes your code to generate graph.log and plot the graph
    """

    # Create the graph
    g = graphviz.Digraph('G', filename='graph.log')
    g.attr(rankdir='LR', size='8,5')

    for i in val:
        g.edge(str(i[0]), str(i[1]))

    # Render the graph
    g.view()


def get_set(val):
    """
    Here goes your code to get the set from the input
    Example: { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    """
    result = None

    try:
        # Use literal_eval to convert the string into a set
        result = ast.literal_eval(val)

        # Check if result is a set
        if not isinstance(result, set):
            raise ValueError("Input string does not represent a set")

    except ValueError as e:
        print(f"Error: Invalid input. {e}")
        raise e
    except Exception as e:
        print("Error: Something went wrong.")
        raise e

    return result


def main():
    print("Hello World analyzing input!")
    # Example: 	{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
    val = input("Enter your set: ")
    val = get_set(val)
    print(val)
    Reflexive, Symmetric, Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(val)


if __name__ == "__main__":
    main()
