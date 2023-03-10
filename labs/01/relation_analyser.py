'''
Author: Carlos David Amezcua Canales (A01641742)
Date: March 9, 2023
Description: 
    This program analyzes a relation and determines if it is reflexive, 
    symmetric, transitive, and of equivalence. It also generates a graph of the 
    relation and displays it.
'''

import graphviz

LOG_FILE_NAME = "graph.log"

def parse_input(string):
    edges = []
    source_node = ""
    destination_node = ""
    state = 0
    for character in string:
        if state == 0:
            if character == '(':
                state = 1
        elif state == 1:
            if character == ',':
                state = 2
            else:
                source_node += character
        elif state == 2:
            if character == ')':
                edges.append((source_node, destination_node))
                source_node = ""
                destination_node = ""
                state = 0
            else:
                destination_node += character
    return edges

def render_graph(edges):
    g = graphviz.Digraph("example", filename=LOG_FILE_NAME)
    g.attr(rankdir="LR")
    g.attr("node", shape="circle")
    for edge in edges:
        g.edge(edge[0], edge[1])
    g.render(engine="dot", format="pdf")

def view_graph():
    g = graphviz.Source.from_file(LOG_FILE_NAME)
    g.view()

def simplify_edges(edges):
    folio = 0
    map = {}
    simplified_edges = []
    for edge in edges:
        for i in range(2):
            if not edge[i] in map:
                map[edge[i]] = folio
                folio += 1
        simplified_edges.append((map[edge[0]], map[edge[1]]))
    return simplified_edges

def create_adj_matrix(simplified_edges):
    num_vertices = 0
    for simple_edge in simplified_edges:
        num_vertices = max(num_vertices, max(simple_edge[0], simple_edge[1]) + 1)
    adj_matrix = [[False for i in range(num_vertices)] for j in range(num_vertices)]
    for simple_edge in simplified_edges:
        adj_matrix[simple_edge[0]][simple_edge[1]] = True
    return adj_matrix

def compute_reflexivity(adj_matrix):
    num_vertices = len(adj_matrix)
    for i in range(num_vertices):
        if not adj_matrix[i][i]:
            return False
    return True

def compute_symmetry(adj_matrix):
    num_vertices = len(adj_matrix)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[i][j] != adj_matrix[j][i]:
                return False
    return True

def compute_transitivity(adj_matrix):
    num_vertices = len(adj_matrix)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[i][j]:
                for k in range(num_vertices):
                    if adj_matrix[j][k] and not adj_matrix[i][k]:
                        return False
    return True

def clasify_relation(adj_matrix):
    is_reflexive = compute_reflexivity(adj_matrix)
    is_symmetric = compute_symmetry(adj_matrix)
    is_transitive = compute_transitivity(adj_matrix)
    is_of_equivalence = is_reflexive and is_symmetric and is_transitive
    return is_reflexive, is_symmetric, is_transitive, is_of_equivalence

def print_clasification(properties):    
    is_reflexive, is_symmetric, is_transitive, is_of_equivalence = properties
    print("(a) R is {}reflexive,".format("" if is_reflexive else "not "))
    print("(b) R is {}symmetric,".format("" if is_symmetric else "not "))
    print("(c) R is {}transitive.".format("" if is_transitive else "not "))
    print("(d) R does {}have equivalence relation"
          .format("" if is_of_equivalence else "not "))

def main():
    edges = parse_input(input())
    render_graph(edges)
    view_graph()
    print_clasification(clasify_relation(create_adj_matrix(simplify_edges(edges))))

if __name__ == "__main__":
    main()
