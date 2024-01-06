import ast
import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

#-----------------------------REFLEXIVA--------------------------------------
def buscando_reflexion(relacion):
    elementos=set()
    for par in relacion:
        elementos.add(par[0])
        elementos.add(par[1])

    for elemento in elementos:
        if (elemento,elemento) not in relacion:
            return "no reflexiva"
    return "reflexiva"

#-----------------------------SIMETRICA--------------------------------------

def buscando_simetria(relacion):
    for par in relacion:
        parReverso=(par[1],par[0])
        if parReverso not in relacion:
            return "no simetrica"
    return "simetrica"
    
#-----------------------------TRANSITIVA--------------------------------------

def buscando_transicion(relacion):
    for primerPar in relacion:
        for segundoPar in relacion:
            if primerPar[1]==segundoPar[0] and (primerPar[0], segundoPar[1]) not in relacion:
                return "no transitiva"
    return "transitiva"

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = buscando_reflexion(val)
    Symmetric = buscando_simetria(val)
    Transitive = buscando_transicion(val)

    return Reflexive, Symmetric, Transitive

def plot(val):
    """
    Here goes your code to generate graph.log and plot the graph
    """

    # Create the graph
    dot= graphviz.Digraph('G', comment='graph.log')
    for i in val:
        dot.edge(str(i[0]), str(i[1]))

    print(dot.source)
    # Render the graph
    dot.view()


def get_set(val):
    """
    How to put the input
    Example:
    {(0,0),(0,1),(0,3),(1,0),(1,1),(2,2),(3,0),(3,3)}
    { (0,0), (1,1), (1,0) }
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
    val = input("Enter your set: ")
    val=get_set(val)
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
