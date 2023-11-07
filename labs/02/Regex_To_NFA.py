import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html
from collections import deque

"""
Name: Juan José Salazar Cortés
ID: A01642126
Date: Monday 03 April 2023

----------------------------------------------------
Hi! Welcome to my solution to Lab 02

The way of input of the regex when beginning the
program must be the next one: 

Example 01: (a U b)* -> (You can use spaces)

Here are some other test cases you could try: 

TestCase 0: a(ab)
TestCase 1: (ab U a)*
TestCase 2: (a U b)
TestCase 3: (ab)
TestCase 4: (abbb)
TestCase 5: (aaaaa)*
TestCase 6: (a U b)*
TestCase 7: (a)*
TestCase 8: (aba U ba)
TestCase 9: (ba)a
TestCase 10: (ba)a*
----------------------------------------------------
"""

# The language that will be used to create the NFA
language = ['a', 'b']

stackRelations = deque()
stackLetters = deque()
stackOperators = deque()

contStates = 0

# Function to Translate the Input Given into Reverse Polish Notation
def regexToPolishNotation(regex):
    for i in range(len(regex)):
        if((regex[i] != '(' and regex[i] != ')') and (regex[i] != ' ' and regex[i] != ' ')):
            if(regex[i] in language):
                stackLetters.append(regex[i])
                if(i != len(regex)-1 and regex[i+1] in language):
                    stackOperators.append('.')
            else:
                stackOperators.append(regex[i])
        if(regex[i] == '(' and i != 0 and regex[i-1] in language):
            stackOperators.append('.')
        if(regex[i] == ')' and i != len(regex)-1 and regex[i+1] in language):
            stackOperators.append('.')

    return

# Function to Create The initial Relations for Each Letter
def simpleLetterConnection(letter):
    global contStates
    stackRelations.append(str(contStates) + str(contStates + 1) + letter + 'F')
    contStates += 2
    return

# Function to concatenate Relations
def concatenation(leftRelations, rightRelations):
    global contStates
    concatenated = []
    concatenated.append(leftRelations)
    concatenated = concatenated[0].split()
    concatenated[-1] = concatenated[-1].replace('F', 'N')
    concatenated.append(leftRelations[-3] + rightRelations[0] + 'Ɛ' + 'N')
    concatenated.append(rightRelations)
    concatenated = ' '.join(concatenated)
    stackRelations.appendleft(concatenated)
    return

# Function to join Relations
def union(leftRelations, rightRelations):
    global contStates
    joined = []
    joined.append(str(contStates) + leftRelations[0] + 'Ɛ' + 'N')
    joined.append(str(contStates) + rightRelations[0] + 'Ɛ' + 'N')
    joined.append(leftRelations)
    joined.append(rightRelations)
    joined = ' '.join(joined)
    stackRelations.appendleft(joined)
    return

# Function to manage the Star Operator
def starOperator(relation):
    global contStates
    starred = []
    contStates += 1
    starred.append(str(contStates) + relation[0] + 'Ɛ' + 'F')
    connectionNode = relation[0]
    relationSplitted = relation.split()
    for i in range(len(relationSplitted)):
        if(relationSplitted[i][-1] == 'F'):
            starred.append(relationSplitted[i][1] + connectionNode + 'Ɛ' + 'N')
    starred.append(relation)
    starred = ' '.join(starred)
    stackRelations.appendleft(starred)
    
#Function to handle all the operations
def operatorHandler():
    if(stackOperators[0] == '.'):
        stackOperators.popleft()
        leftRelations = stackRelations[0]
        stackRelations.popleft()
        rightRelations = stackRelations[0]
        stackRelations.popleft()
        concatenation(leftRelations, rightRelations)

    elif(stackOperators[0] == 'U'):
        stackOperators.popleft()
        leftRelations = stackRelations[0]
        stackRelations.popleft()
        rightRelations = stackRelations[0]
        stackRelations.popleft()
        union(leftRelations, rightRelations)

    else:
        stackOperators.popleft()
        relation = stackRelations[0]
        stackRelations.popleft()
        starOperator(relation)

    return

# Function to Create All connections Between Nodes
def stackRelationsCreator():
    for i in range(len(stackLetters)):
        simpleLetterConnection(stackLetters[i])
    while(len(stackOperators) > 0):
        operatorHandler()
    return

# Function to Plot the Relations in StackRelations
def plotNFA(stackRelations):
    NFA = graphviz.Digraph('NFA', filename='NFA.log')
    NFA.attr(rankdir='LR')
    for i in range(len(stackRelations)):
        if(len(stackRelations[i]) > 3):
            relationSplitted = stackRelations[i].split()
            for j in range(len(relationSplitted)):
                if(len(relationSplitted[j]) > 4):
                        if(relationSplitted[j][4] == 'F'):
                            NFA.node(relationSplitted[j][0] + relationSplitted[j][1], shape='circle')
                            NFA.node(relationSplitted[j][2], shape='doublecircle')
                            NFA.edge(relationSplitted[j][0] + relationSplitted[j][1], relationSplitted[j][2], label=relationSplitted[j][3])
                        else:
                            NFA.node(relationSplitted[j][0] + relationSplitted[j][1], shape='circle')
                            NFA.edge(relationSplitted[j][0] + relationSplitted[j][1], relationSplitted[j][2], label=relationSplitted[j][3])
                else:
                        if(relationSplitted[j][3] == 'F'):
                            NFA.node(relationSplitted[j][0], shape='circle')
                            NFA.node(relationSplitted[j][1], shape='doublecircle')
                            NFA.edge(relationSplitted[j][0], relationSplitted[j][1], label=relationSplitted[j][2])
                        else:
                            NFA.node(relationSplitted[j][0], shape='circle')
                            NFA.edge(relationSplitted[j][0], relationSplitted[j][1], label=relationSplitted[j][2])
            if(len(relationSplitted[0]) > 4):
                if(relationSplitted[0][4] == 'F'):
                    NFA.node(relationSplitted[0][0] + relationSplitted[0][1], shape='doublecircle')
                    NFA.node(relationSplitted[0][2], shape='circle')
            else:
                if(relationSplitted[0][3] == 'F'):
                    NFA.node(relationSplitted[0][0], shape = 'doublecircle')
                    NFA.node(relationSplitted[0][1], shape = 'circle')
        else: 
            if(stackRelations[i][3] == 'F'):
                NFA.node(stackRelations[i][0], shape='circle')
                NFA.node(stackRelations[i][1], shape='doublecircle')
                NFA.edge(stackRelations[i][0], stackRelations[i][1], label=stackRelations[i][2])
            else:
                NFA.node(stackRelations[i][0], shape='circle')
                NFA.edge(stackRelations[i][0], stackRelations[i][1], label=stackRelations[i][2])
    NFA.view()
    return

def main():
    print("\n------- Hi! If you want to try some test cases copy and paste some from the comment at the top of the code :) --------")
    regex = input("\nEnter your Regex: ")

    regexToPolishNotation(regex)
    stackRelationsCreator()
    plotNFA(stackRelations)

if __name__ == "__main__":
    main()
