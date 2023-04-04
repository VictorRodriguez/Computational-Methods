import re
import graphviz #https://graphviz.readthedocs.io/en/stable/index.html

#Nolberto Castro Sánchez
#A01641501
#31 de Marzo del 2023
#Lab-02

class Node:
    def __init__(self, start, end, label):
        self.start = start
        self.end = end
        self.label = label

#Input Regex and reparation
REGEX = input('Enter your REGEX: ').replace(" ", "")
print("Hello!!!! analyzing input!")
values = sorted(set(re.sub(r'[*+?|uU∪(), ]', '', REGEX)))

#Defining the stacks
endNodes = ['0']
unions = []
counter = 0
sNode = counter
eNode = counter + 1
index = 0

#Verify the operation to follow
def checkNext(condition):
    global index
    if index + 1 < len(REGEX):
        return REGEX[index + 1] == condition
    return False

#Regex Analizer
def regexAnalizer(pNode):
    global endNodes, unions, counter, sNode, eNode, index
    currentNode = None
    endNode = None

    while index < len(REGEX):
        char = REGEX[index]

        if char in values:
            currentNode = Node(sNode, eNode, char)
            unions.append(currentNode)
            counter += 1

            if checkNext('*'):
                index += 1
                unions.append(Node(currentNode.end, currentNode.end, char))
                if endNode:
                    counter += 1
                    current_aux = Node(currentNode.start, counter, 'ε')
                    unions.append(current_aux)
                    unions.append(Node(currentNode.end, counter, 'ε'))
                    currentNode = current_aux

            sNode = counter
            eNode = counter + 1
            endNode = currentNode
        elif char == '(':
            index += 1
            endNode = regexAnalizer(currentNode.end if currentNode else pNode)
        elif char == ')':
            if checkNext('*'):
                index += 1
                unions.append(Node(pNode, currentNode.end, 'ε'))
                if endNode:
                    counter += 1
                    unions.append(Node(currentNode.end, pNode, 'ε'))
            endNode = currentNode
            break
        elif char.upper() in ['U', '|', '∪']:
            endNodes.append(str(currentNode.end))
            sNode = pNode
            eNode = endNode.end
        index += 1
    return endNode

#Defining the end states of our NFA
endStates = regexAnalizer(0)
if str(endStates.end) not in endNodes:
    endNodes.append(str(endStates.end))
eNodes = ' '.join(endNodes)

#Graphication
def graphVizTraduction(unions, eNodes):
    base = '''
    digraph finite_state_machine {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]
        rankdir=LR;
    '''
    base += f'''
        node [shape = doublecircle]; {eNodes};
        node [shape = circle]; 
    '''
    for union in unions:
        base += f'\n\t{union.start} -> {union.end} [label = "{union.label}"];'
    base += '\n}'
    print(base)


#graphication
graphVizTraduction(unions, eNodes)

