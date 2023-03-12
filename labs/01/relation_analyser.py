"""Mariana Esquivel Hernandez A01641244 - 03/11/2023 - 1st Lab - Reflexivity, Symmetry and Transitivity

    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
"""
import graphviz # https://graphviz.readthedocs.io/en/stable/index.html
import re

def reflexive(values_set, aux_set):
    is_reflexive = True
    for aux in aux_set:
        aux_tuple = (aux, aux)

        if aux_tuple not in values_set:
            is_reflexive = False
            print(str(aux_tuple) + ' : ')
            break

    if is_reflexive:
        print('Reflexive')
    else:
        print('Not reflexive')
    return is_reflexive, aux_tuple

def symmetric(values_set):
    is_symmetric = True
    for value in values_set:
        aux_tuple = (value[1], value[0])

        if aux_tuple not in values_set:
            is_symmetric = False
            print(str(aux_tuple) + ' : ')
            break

    if is_symmetric:
        print('Simetric')
    else:
        print('Not simetric')

    filtered_set = [x for x in values_set if x[0] != x[1]]

    return is_symmetric, filtered_set

def transitive(values_set, filtered_set):
    is_transitive = True
    for value in filtered_set:
        aux_list = [x for x in filtered_set if x[0] == value[1] and x != (value[1], value[0])]
        if len(aux_list) > 0:
            for aux_value in aux_list:
                aux_tuple = (value[0], aux_value[1])
                if aux_tuple not in values_set:
                    is_transitive = False
                    print(str(aux_tuple) + ' : ')
                    break
        else:
            print(str(value) + ' : ')
            is_transitive = False

        if not is_transitive:
            break

    if is_transitive:
        print('Its trasitive')
        return True
    else:
        print('Not trasitive')
        return False

def plot(values_set):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graph.gv')
    for n in values_set:
        start = n[0]
        end = n[1]
        g.edge(str(start), str(end))    
    g.view()

def log(values_set):
    f = open('graph.log', 'x')
    f.write("""digraph example {\nrankdir=LR;
        node [shape = circle];\n""")
    for n in values_set:
        start = n[0]
        end = n[1]
        f.write(str(start) + ' -> ' + str(end) + ';\n')
    f.write("\n}")
    f.close()

def main():
    print("Hello World analyzing input!")
    input_value = input("Enter your set: ") # { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3), (1,3), (3,1) }
    print(input_value)
    values = re.sub(r'[{}(), ]', '', input_value)

    values_set = set()

    aux_set = set()

    for value in values:
        aux_set.add(int(value))

    for i in range(0, len(values), 2):
        values_tuple = (int(values[i]), int(values[i + 1]))
        values_set.add(values_tuple)

    # stringToTuple(input_value)

    # print(f"\
    # 1. Reflexive: {reflexive} \
    # 2. Symmetric: {symmetric} \
    # 3. Transitive: {transitive}")

    reflexive(values_set, aux_set)
    symmetric(values_set)
    transitive(values_set, symmetric(values_set)[1])

    # if reflexive and symmetric and transitive:
    #     print('Equivalence relation')
    # else:
    #     print('Not equivalence relation')
    plot(values_set)
    log(values_set)


if __name__ == "__main__":
    main()
