"""Mariana Esquivel Hernandez A01641244 - 04/03/2023 - 2nd Lab
EQUIVALENCE WITH FINITE AUTOMATA - "REGULAR EXPRESSION TO NOTATION"""

import re
# import graphviz  # doctest: +NO_EXE

# Dictionary
# ε empty
# | or
# * empty, one or more
# U Union

# examples:
# a                 S -> a -> E
# abb               S -> a -> b -> b -> E
# (abb)*            S -> a -> b -> b -> E
#                        |         |
#                        ----------
# a(abb)*           S -> a -> a -> b -> b -> E
#                             |         |
#                             ----------
# a(abb*)Ub         S -> a -> a -> b -> b -> E
#                   |         |         |
#                   b         ----------
#                   |
#                   E

base = '''
digraph finite_state_machine {
    fontname="Helvetica,Arial,sans-serif"
    node [fontname="Helvetica,Arial,sans-serif"]
    edge [fontname="Helvetica,Arial,sans-serif"]
    rankdir=LR;
'''
# a(abb*)*


class Union:
    def __init__(self, start, end, label):
        self.start = start
        self.end = end
        self.label = label

print("""\nEQUIVALENCE WITH FINITE AUTOMATA - "REGULAR EXPRESSION TO NOTATION"\n
ALPHABET: {a,b} | {0,1}\nREGULAR EXPRESSIONS SYMBOLS: (, ), *, +, |\nUNION SYMBOL: U\n
EXAMPLE OF INPUT "REGULAR EXPRESSION": (ab U a)*\n""")

regular_expression = input('Regular expression: ').replace(" ", "")
values = sorted(set(re.sub(r'[*+?|uU∪(), ]', '', regular_expression)))

last_nodes = ['0']
unions = []
counter = 0
start_node = counter
end_node = counter + 1
index = 0


def verify_next_char(operation):
    global index
    if index + 1 < len(regular_expression):
        return regular_expression[index + 1] == operation
    return False


def union_nodes(parent_node):
    global last_nodes, unions, counter, start_node, end_node, index
    current_union = None
    last_union = None

    while index < len(regular_expression):
        char = regular_expression[index]

        if char in values:
            current_union = Union(start_node, end_node, char)
            unions.append(current_union)
            counter += 1

            if verify_next_char('*'):
                index += 1
                unions.append(Union(current_union.end, current_union.end, char))
                if last_union:
                    counter += 1
                    current_aux = Union(current_union.start, counter, 'ε')
                    unions.append(current_aux)
                    unions.append(Union(current_union.end, counter, 'ε'))
                    current_union = current_aux

            start_node = counter
            end_node = counter + 1
            last_union = current_union
        elif char == '(':
            index += 1
            last_union = union_nodes(current_union.end if current_union else parent_node)
        # elif char == '+':
        #     index += 1
        #     current_union = Union(current_union.start, current_union.end, regular_expression[index])
        #     unions.append(current_union)
        elif char == ')':
            if verify_next_char('*'):
                index += 1
                unions.append(Union(parent_node, current_union.end, 'ε'))
                if last_union:
                    counter += 1
                    unions.append(Union(current_union.end, parent_node, 'ε'))
            last_union = current_union
            break
        elif char.upper() in ['U', '|', '∪']:
            last_nodes.append(str(current_union.end))
            start_node = parent_node
            end_node = last_union.end

        index += 1

    return last_union


final_node = union_nodes(0)

# Graph
# dot = graphviz.Digraph(comment='The Round Table')

if str(final_node.end) not in last_nodes:
    last_nodes.append(str(final_node.end))

end_nodes = ' '.join(last_nodes)

base += f'''
    node [shape = doublecircle]; {end_nodes};
    node [shape = circle]; 
'''

for union in unions:
    # dot.edge(str(union.start), str(union.end), label=union.label)
    base += f'\n\t{union.start} -> {union.end} [label = "{union.label}"];'
base += '\n}'

print(base)
