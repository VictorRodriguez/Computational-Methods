# Emily Rosenfeld, A01198339
# ACT 01

def analyze(val):

    # Asi convertimos val en una tupla
    val = eval(val)

    # Poner las condiciones iniciales en False
    Reflexive = False
    Symmetric = False
    Transitive = False
    m = 0

    # Aqui se revisara la Refelexividad del conjunto de tuplas
    for a,b in val:
        if (a, a) not in val:
            m += 1
            break
        elif (b, b) not in val:
            m += 1
            break
    if m == 0:
        Reflexive = True

    # Aqui se revisara la Simetria del conjunto de tuplas
    Symmetric = False
    for a,b in val :
        if (a, b) and (b, a) not in val:
            Symmetric = False
            break
        else:
            Symmetric = True

    # Aqui se revisara la Transitividad del conjunto de tuplas
    Transitive = False
    for a, b1 in val:
        for b2, c in val:
            if (b1 == b2) and (b1 != a) and (b1 != c) and (a != c) and (c, a) not in val:
                Transitive = False
                break
            else:
                Transitive = True

    return Reflexive, Symmetric, Transitive

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)

    Reflexive, Symmetric, Transitive = analyze(val)

    if ((Reflexive == True) and (Symmetric == True) and (Transitive == True)):
        Equivalence = True
    else:
        Equivalence = False


    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive} \
    4. Equivalence: {Equivalence}  ")

    # Imprimir el grafo 
    print("\n\n digraph example { \n rankdir=LR; \n node [shape = circle];\n")
    val = eval(val)
    for a,b in val:
        print(f"  {a} -> {b} ;")
    print("\n\n}")


if __name__ == "__main__":
    main()
