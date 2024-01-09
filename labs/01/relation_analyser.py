#Tuve problemas instalando graphviz por lo que decidi generar un archivo de texto para que lo pueda copiar y pegar en Graphviz online

def analyze(val):

    Reflexivo = all((a, a) in val for a, _ in val)
    Simetrico = all((b, a) in val for a, b in val)
    Transitivo = all((a, c) in val for a, b1 in val for b2, c in val if b1 == b2)

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
