"""
Rodrigo López Guerra
A01737437

Description: This program analyzes tuples in a sequence of a set. It organizes each
tuples and receive the elements of the tuple in order to determine the relations
around the sequence. As well, it creates a map which will allow us to visualize the
relations in a better way.

Inputs: You can write the sequence of tuples separated with commas, however the
program will respect the order of the elements in the input and organize this one
into a readable sequence.
"""

# LIBRARIES
import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html
import random

nodes = []


# FUNCTIONS
# FUNCTION: CONVERT LIST INTO TUPLES, REMOVES DUPLICATES, ORDERS TUPLES,
# AND TRANSFORMS TUPLES INTO A FLAT LIST
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n log n)
def transformation(val):
    # Deletes every string that isn't a comma or an integer
    while True:
        try:
            val = ''.join(str(i) for i in val if i.isdigit() or i == ',')
            val = [int(i) for i in val.split(',')]
        except ValueError as e:
            print(f"ERROR: {e}")
            val = input("Invalid input. Remember to separate each number by commas. Try again: ")
        else:
            if len(val) % 2 == 1:
                val.append(0)
            break
    tuples = [(val[i], val[i + 1]) for i in range(0, len(val), 2)]
    tuples = list(set(tuples))
    tuples.sort()

    for i in range(len(val)):
        if val[i] not in nodes:
            nodes.append(val[i])

    return [item for tup in tuples for item in tup]


# FUNCTION: PRINT THE COHERENT SEQUENCE OF TUPLES
# COMPLEXITY: O(n)
def print_conj(val):
    print("{", end="")
    for i in range(len(val)):
        if i % 2 == 0:
            print("(" + str(val[i]) + ",", end="")
        else:
            print(str(val[i]) + ")", end="")
            if i != len(val) - 1:
                print(",", end="")
    print("}")


# FUNCTION: ANALYSE THE RELATION
# COMPLEXITY: O(n)
def send_relation_dict(val):
    relation_dict = {}
    for i in range(0, len(val), 2):
        a, b = val[i], val[i + 1]
        if a in relation_dict:
            relation_dict[a].add(b)
        else:
            relation_dict[a] = {b}
    return relation_dict


# FUNCTION: ANALYSE IF THE RELATION IS REFLEXIVE
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n*m)
def reflexive_relations(relation_dict):

    status = False
    check = 0

    for a, related_a in relation_dict.items():
        for b in related_a:
            for i in nodes:
                if a == i or b == i:
                    check += 1
                    status = True
            if a != b and check != len(nodes):
                status = False

    return status


# FUNCTION: ANALYSE IF THE RELATION IS SYMMETRIC
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n*m)
def symmetric_relations(relation_dict):
    status = False
    check = False

    for a, related_a in relation_dict.items():
        for b in related_a:
            if a == b and check is False:
                status = False
            elif b not in relation_dict or a not in relation_dict[b]:
                status = False
                return status
            else:
                status = True
                check = True

    return status


# FUNCTION: ANALYSE IF THE RELATION IS SYMMETRIC
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n*m²)
def transitive_relations(relation_dict):
    status = False
    check = False

    for a, related_a in relation_dict.items():
        for b in related_a:
            if b in relation_dict:
                for c in relation_dict[b]:
                    if c in relation_dict[a]:
                        status = True
                        check = True
                    elif a == b and check is False:
                        status = False
                    else:
                        status = False
                        return status

    return status


# FUNCTION: ANALYSE THE SEQUENCE
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n*m²)
def analyze(value):
    relation_dict = send_relation_dict(value)
    reflexive = reflexive_relations(relation_dict)
    symmetric = symmetric_relations(relation_dict)
    transitive = transitive_relations(relation_dict)

    # CASE: EQUIVALENCE
    if reflexive and symmetric and transitive:
        equivalence = True
    else:
        equivalence = False

    return reflexive, symmetric, transitive, equivalence


# FUNCTION: CREATES A GRAPH WITH THE PREVIOUS RELATIONS
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n²)
def plot(val):
    g = graphviz.Digraph(filename='graph.log')
    colors = ['#FFA07A', '#F0E68C', '#D8BFD8', '#98FB98', '#FAF0E6', '#AFEEEE', '#FFA500', '#FF69B4', '#DC143C',
              '#A9A9A9']

    for j in nodes:
        g.attr(rankdir='LR')
        g.node(str(j), style='filled', fillcolor=random.choice(colors), shape='circle')

    for i in range(len(val)):
        if i % 2 == 0:
            g.edge(str(val[i]), str(val[i + 1]))

    try:
        g.view()
    except graphviz.ExecutableNotFound as e:
        print("ERROR:", e)
        print("The graph could not be rendered. Please check your Graphviz installation and try again.")
        print("Go to https://dreampuf.github.io/GraphvizOnline/ and copy the content on graph.log to visualize.")


# FUNCTION: MAIN
# COMPLEXITY: BEST CASE - O(n) | WORST CASE - O(n*m²)
def main():
    global nodes

    print("Running Program!")
    val = input("Enter your set: ")
    val = transformation(val)

    print_conj(val)

    reflexive, symmetric, transitive, equivalence = analyze(val)
    print(f"\n \
    1. Reflexive: {reflexive} \n \
    2. Symmetric: {symmetric} \n \
    3. Transitive: {transitive} \n \
    4. Equivalence: {equivalence}")
    plot(val)


if __name__ == "__main__":
    main()
