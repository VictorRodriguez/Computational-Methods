import graphviz # https://graphviz.readthedocs.io/en/stable/index.html
import os

def analyze(val):
    """
    Analiza la relación para reflexividad, simetría y transitividad.
    """
    relation = set(eval(val))
    elements = set(x for a, b in relation for x in (a, b))

    Reflexive = all((x, x) in relation for x in elements)
    Symmetric = all((b, a) in relation for a, b in relation)
    Transitive = all((a, c) in relation for a, b in relation for c, d in relation if b == c)

    return Reflexive, Symmetric, Transitive

def plot(val):
    """
    Crea y muestra el gráfico de la relación e imprime el código fuente de Graphviz.
    """
    # Analiza la entrada a un conjunto de tuplas.
    relation = set(eval(val))

    # Inicializa el Digraph de Graphviz.
    g = graphviz.Digraph('G', filename='graph.gv')
    g.attr(rankdir='LR', node_shape='circle')

    # Bucle para añadir aristas al gráfico.
    for a, b in relation:
        g.edge(str(a), str(b))

    # Imprime el código fuente de Graphviz en la consola.
    print(g.source)

    # Genera y renderiza el gráfico.
    # El gráfico se guardará como 'graph.png'.
    g.render(filename='graph', format='png', cleanup=True)

    # Abre automáticamente la imagen del gráfico generada.
    os.system("open graph.png")

def main():
    val = input("Introduce tu conjunto: ")
    print(val)
    Reflexive, Symmetric, Transitive = analyze(val)
    print(f"1. Reflexivo: {Reflexive} \
    \n2. Simétrico: {Symmetric} \
    \n3. Transitivo: {Transitive}")

    # Llama a la función plot con el valor de entrada.
    plot(val)

if __name__ == "__main__":
    main()
