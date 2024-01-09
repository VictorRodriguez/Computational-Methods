#Tuve problemas instalando graphviz por lo que decidi generar un archivo de texto para que lo pueda copiar y pegar en Graphviz online

def analyze(val):
    Reflexivo = False
    Simetrico = False
    Transitivo = False

    for pair in val:
        a, b = pair

        # condicional para ver si es reflexivo
        if a == b or (a, a) in val:
            Reflexivo = True

        # condicional para ver si es simétrico
        if (b, a) in val:
            Simetrico = True

    # condicional para ver si es transitivo
    for pair_1 in val:
        a, b = pair_1
        for pair_2 in val:
            c, d = pair_2
            if b == c and (a, d) not in val:
                Transitivo = False
                break

    return Reflexivo, Simetrico, Transitivo

def text_graph(val):
    with open('graph.txt', 'w') as file:
        file.write('Digraph {\n')

        for pair in val:
            file.write(f'\t{pair[0]} -> {pair[1]} ;\n')

        file.write('}\n')

def main():
    print("Set:")
    val_str = input("Ingresa tu set en el formato { (a,b), (c,d), (e,f) ... }: ")
    val = eval(val_str)  # Convierte string a una tupla

    Reflexivo, Simetrico, Transitivo = analyze(val)

    if Reflexivo:
        print("R es reflexivo.")
    else:
        print("R no es reflexivo.")

    if Simetrico:
        print("R es simetrico.")
    else:
        print("R no es simetrico.")

    if Transitivo:
        print("R es transitivo.")
    else:
        print("R no es transitivo.")

    if Reflexivo and Simetrico and Transitivo:
        print("R tiene una relación equivalente")

    text_graph(val)

if __name__ == "__main__":
    main()
