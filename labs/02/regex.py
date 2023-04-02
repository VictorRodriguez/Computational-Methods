# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:14:07 2023

@author: jusus
"""

import graphviz # https://graphviz.readthedocs.io/en/stable/index.html
import sys

print("Regular expression to notation")

print("Alphabet: {0,1} or {a,b}")

print("Remember to only use ONE of the alphabets, DO NOT COMBINE")

print("Union symbol: U")

print("Example of Input string : (ab ∪ a)*")

regex = input("Enter the regular expression: ")

parenthesis_number = 0
alphabet_a = False
alphabet_0 = False
regex_error = False

# Checks if regex has valid parentheses
# Exits the program if it doesn't
for i in regex:
    if (i == 'a' or i == 'b'):
        alphabet_a = True
    if (i == '0' or i == '1'):
        alphabet_0 = True
    if i == '(':
        parenthesis_number += 1
    if i == ')':
        parenthesis_number -= 1
    elif i == ')' and parenthesis_number == 0:
        regex_error = True


if(parenthesis_number != 0):
    regex_error = True
if(alphabet_a == True and alphabet_0 == True):
    regex_error = True
if(alphabet_a == False and alphabet_0 == False):
    regex_error = True

if(regex_error == True):
    sys.exit("Input error (parentheses or wrong alphabet)")


# Graphviz graph
g = graphviz.Digraph('G', filename='NFA.gv')
g.attr('node', shape='circle')

# Variables that help check number of nodes
nodes = []
total_nodes = 0
node_has_edge = []

# Creates a starting automata with most states
for i in regex:
    if(i == 'a' or i == 'b' or i == '0' or i == '1' or i == 'E'):
        total_nodes += 1
x = 0
while x != total_nodes + 3:
    nodes.append('q'+str(x))
    node_has_edge.append(False)
    x+=1

# Starts the variables that will help form the edges and makes a starting edge
# to have an empty start state
start_node = 0
next_node = 1
end_node = total_nodes
g.node(nodes[start_node])
g.edge(nodes[start_node], nodes[next_node], label = 'E')
node_has_edge[start_node] = True
curr_node = start_node + 1
open_node = curr_node
next_node += 1

# variables that will help with parentheses
parenthesis_start_nodes = []
parenthesis_end_nodes = []
parenthesis_end_nodes_history = []
parenthesis_counter = 0
last_parenthesis = False
end_points = 0
had_op = False
reg_counter = -1
dont_check = False

parenthesis_group_numbers = []
parenthesis_group_num = 0
parenthesis_inside = []

node_parenthesis = []

def go_throuh_paren_numbers(x):
    count = 0
    for i in parenthesis_group_numbers:
        if (i == x):
            count += 1
    return count

def search_open_paren():
    for i in reversed(parenthesis_group_numbers):
        found = False
        count = 0
        for k in reversed(parenthesis_group_numbers):
            if (i == k):
                if(count == 0):
                    count = 1
                else:
                    found = True
        if(found == False):
            return i
                

for i in regex:
    reg_counter += 1
    if(i == '*'):
        if(last_parenthesis == True):
            top = len(parenthesis_group_numbers)
            appending = False
            for i in parenthesis_group_numbers:
                if(i == parenthesis_group_numbers[top-1]):
                    if(appending == False):
                        appending = True
                    else:
                        appending = False
                if(appending == True):
                    parenthesis_inside.append(i)
            nodes.append('q'+str(x))
            x+=1
            g.edge(nodes[curr_node], nodes[next_node], label = 'E')
            node_has_edge[curr_node] = True
            curr_node += 1
            next_node += 1
            temp = len(parenthesis_group_numbers)
            if(parenthesis_group_numbers[0] != parenthesis_group_numbers[temp-1]):
                print("ENTERED")
                for i in parenthesis_end_nodes:
                    if i in parenthesis_inside:
                        open_node = i
                        break
            g.edge(nodes[curr_node], nodes[open_node], label = 'E')
            node_has_edge[curr_node] = True
            g.edge(nodes[open_node], nodes[curr_node], label = 'E')
            node_has_edge[open_node] = True
            counter = 0
            for i in parenthesis_end_nodes:
                if(node_parenthesis[counter] in parenthesis_inside and node_has_edge[i] == False):
                    g.edge(nodes[i], nodes[curr_node], label = 'E')
                    node_has_edge[i] = True
            parenthesis_end_nodes.clear()
            node_parenthesis.clear()
            last_parenthesis = False
            had_op = True
        else:
            g.edge(nodes[curr_node], nodes[curr_node-1], label = 'E')
            g.edge(nodes[curr_node-1], nodes[next_node], label = 'E')
            g.edge(nodes[curr_node], nodes[next_node], label = 'E')
            node_has_edge[curr_node] = True
            next_node += 1
            curr_node += 1
            nodes.append('q'+str(x))
            x+=1
    elif(i == 'a' or i == 'b' or i == '0' or i == '1'):
        tail = nodes[curr_node]
        head = nodes[next_node]
        g.edge(tail, head, label=(i))
        node_has_edge[curr_node] = True
        curr_node += 1
        next_node += 1
    elif(i == 'U'):
        if(last_parenthesis == True):
            last_parenthesis = False
            had_op = True
        curr_node = start_node
        g.edge(nodes[curr_node], nodes[next_node], label = 'E')
        node_has_edge[curr_node] = True
        curr_node = next_node
        open_node = curr_node
        next_node += 1
        total_nodes+=1
        nodes.append('q'+str(x))
        node_has_edge.append(False)
        x+=1
        if(end_points == True):
            if(curr_node not in parenthesis_end_nodes_history):
                parenthesis_end_nodes.append(curr_node-1)
                end_node_inside = search_open_paren()
                node_parenthesis.append(end_node_inside)
                parenthesis_end_nodes_history.append(curr_node-1)
    elif(i == '('):
        parenthesis_group_num += 1
        parenthesis_group_numbers.append(parenthesis_group_num)
        parenthesis_start_nodes.append(curr_node-1)
        parenthesis_counter += 1
        end_points += 1
    elif(i == ')'):
        done = False
        num = 0
        while(done == False):
            count = go_throuh_paren_numbers(parenthesis_group_num-num)
            if(count == 2):
                num += 1
            else:
                parenthesis_group_numbers.append(parenthesis_group_num-num)
                done = True
        end_points -= 1
        open_node = parenthesis_start_nodes[parenthesis_counter-1]
        last_parenthesis = True
        parenthesis_counter -= 1
        if(end_points > 0):
            if(curr_node not in parenthesis_end_nodes_history):
                parenthesis_end_nodes.append(curr_node)
                end_node_inside = search_open_paren()
                node_parenthesis.append(end_node_inside)
                parenthesis_end_nodes_history.append(curr_node)
        if(reg_counter +1 == len(regex)):
            dont_check = True
        if(dont_check == False):
            if(regex[reg_counter + 1] == '*'):
                parenthesis_end_nodes.append(curr_node)
                end_node_inside = search_open_paren()
                node_parenthesis.append(end_node_inside)
                parenthesis_end_nodes_history.append(curr_node)
        elif(end_points == 0 and had_op == True):
            for i in parenthesis_end_nodes:
                if(i != curr_node):
                    g.edge(nodes[i], nodes[curr_node], label = 'E')
                    node_has_edge[i] = True
            parenthesis_end_nodes.clear()
            node_parenthesis.clear()
        had_op = False

g.edge(nodes[curr_node], nodes[next_node], label = 'E')
node_has_edge[curr_node] = True

edge_check = 0
while edge_check != len(node_has_edge) - 1:
    if node_has_edge[edge_check] == False:
        g.edge(nodes[edge_check], nodes[x-1], label = 'E')
    edge_check += 1
    
g.node(nodes[x-1], shape='doublecircle')

for i in node_parenthesis:
    print(i)

    
g.view()




