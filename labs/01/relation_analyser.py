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
            if primerPar[1]==segundoPar[0]:
                 parCompuesto=(primerPar[0], segundoPar[1])
                 if parCompuesto not in relacion:
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
"""
def plot(val):
    #Here goes your code to generate graph.log and plot the graph

    # Create the graph
    dot= graphviz.Digraph('G', comment='graph.log')
    for i in val:
        dot.edge(str(i[0]), str(i[1]))

    print(dot.source)
    # Render the graph
    #dot.view()
    #decidi imprimir el log de la relacion porque me di cuenta que en codespace al generar el pdf 
    #para la accion de abrir en otra pestaña el archivo

"""
def plot(val, output_file='graph.gv'):
    """
    Generate graph.log and save the DOT source code to a .gv file

    Decidi imprimir el log de la grafica y guardarlo en un .gv porque al usar el comando view 
    me aparecia un error al generar el pdf
    """

    #Create the graph
    dot=graphviz.Digraph('G',comment='graph.log')
    for i in val:
        dot.edge(str(i[0]),str(i[1]))

    #Save the graph into graph.gv 
    with open(output_file,'w') as file:
        file.write(dot.source)

    print(f'Graph was saved into file {output_file}')

def checking_theSet(val):
    """
    How to put the input
    Example:
    {(0,0),(0,1),(0,3),(1,0),(1,1),(2,2),(3,0),(3,3)}
    { (0,0), (1,1), (1,0) }
    """
    checkedSet=None

    try:
        #Using literal_eval to convert the input string to a set
        checkedSet=ast.literal_eval(val)

        # Check if result is a set
        if not isinstance(checkedSet,set):
            raise ValueError("Input is not a set")

    except ValueError as e:
        print(f"Invalid input. {e}")
        raise e
    except Exception as e:
        print("Something went wrong.")
        raise e

    return checkedSet

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    val=checking_theSet(val)
    print(val)
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    #plot(val)
    plot(val, 'graph.gv')

if __name__ == "__main__":
    main()
