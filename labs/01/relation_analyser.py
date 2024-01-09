import networkx as nx
import matplotlib.pyplot as plt
import itertools

def analyze(val):
    """
    Aquí va tu código para realizar el análisis.
    1. Reflexiva: aRa para todo a en X,
    2. Simétrica: aRb implica bRa para todo a, b en X
    3. Transitiva: aRb y bRc implica aRc para todo a, b, c en X
    """
    Reflexiva = all((a, a) in val for a, _ in val)
    Simetrica = all((b, a) in val for a, b in val)
    Transitiva = all((a, c) in val for a, b in val for _, c in val if b == _)

    return Reflexiva, Simetrica, Transitiva, val

def plot(relation):
    """
    Aquí va tu código para realizar la representación gráfica del conjunto.
    """
    g = nx.DiGraph()
    g.add_edges_from(relation)
    nx.draw(g, with_labels=True, font_weight='bold')
    plt.show()

def main():
    print("Hola mundo analizando entrada!")
    val = eval(input("Ingresa tu conjunto en el formato [(a, b), (c, d), ...]: "))
    print(val)
    Reflexiva, Simetrica, Transitiva, relation = analyze(val)
    print(f"\
    1. Reflexiva: {Reflexiva} \
    2. Simétrica: {Simetrica} \
    3. Transitiva: {Transitiva}")
    if not (Reflexiva and Simetrica and Transitiva):
        print("La relación no es simétrica y reflexiva, por lo que no tiene una relación de equivalencia.")
    else:
        plot(relation)

if __name__ == "__main__":
    main()
