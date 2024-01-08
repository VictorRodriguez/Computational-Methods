# Implementación de métodos computacionales 
# Diego Alejandro Anaya Alanis, A01663765, 08/01/2024

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html
import xdg 

def analyze(val):
    
    numbers = set()
    for value in val:
        numbers.add(value[0])
        numbers.add(value[1])

    reflexive = set()
    for number in numbers:
        reflexive.add((number,number))
    Reflexive = False
    for i in reflexive:
        if i in val:
            Reflexive = True
        else:
            Reflexive = False
    
    Symmetric = False
    for value in val:
        s = (value[1],value[0])
        if s in val:
            Symmetric = True
        else: 
            Symmetric = False

    Transitive = False
    for x, y in val:
        for x_prima, y_prima in val:
            if y == x_prima:
                if (x, y_prima) in val:
                    Transitive = True
            else:
                Transitive = False

    return Reflexive,Symmetric,Transitive

def plot(val):
    g = graphviz.Digraph('G', format='png', filename='hello.gv')


    numbers = set()
    for value in val:
        numbers.add(value[0])
        numbers.add(value[1])

    for number in numbers:
        g.node(str(number))


    for pair in val:
        g.edge(str(pair[0]), str(pair[1]))


    g.render(filename='graph', cleanup=True)
    print("Graph generated . Check 'graph.png'.")

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    numeros = val.replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace(' ', '')
    numeros = numeros.split(',')
    val = {(int(numeros[i]), int(numeros[i + 1])) for i in range(0, len(numeros), 2)}
    Reflexive,Symmetric,Transitive = analyze(val)
    print(f"\
    1. R is Reflexive: {Reflexive} \
    2. R is Symmetric: {Symmetric} \
    3. R is Transitive: {Transitive}")
    plot(val)

if __name__ == "__main__":
    main()
