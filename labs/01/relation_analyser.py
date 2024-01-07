"""
 @Miguel Angel Cabrera Victoria <A01782982@tec.mx>
 Input : {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)}
        {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3), (4,1), (4,4), (5,5)}
"""
import graphviz 

def reflexive(pair_lists):
    result = []
    max = 0
    for element in pair_lists:
        if element[0] == element[1]:
            max = element[0]
            result.append([element[0],element[1]])
        
    #print("Result ", len(result))
    if len(result) == max + 1:
        return True
    return False

def transitive(pair_lists):
    pass

#------------------------------------------------------------

def plot(pair_lists):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graph.gv')

    for pair in pair_lists:
        # print(pair[0], " ", pair[1])
        g.edge(str(pair[0]), str(pair[1]))
    #g.view()


    
    Reflexive = reflexive(pair_lists)
    #print(Reflexive)
    # print(f"\
    # 1. Reflexive: {Reflexive} \
    # 2. Symmetric:  \
    # 3. Transitive:")
    plot(pair_lists)

def main():
    print("Miguel Angel Cabrera Victoria - A01782982")
    val = input("Enter your set: ")

    pairs = [pair.replace("{", "").replace("}", "").replace("(", "").replace(")", "").strip(',') for pair in val.split(" ")]
    #print(pairs)
    pair_lists = [[int(element) for element in pair.split(',')] for pair in pairs]
    #print(pair_lists)

    # Output 
    
    Reflexive = reflexive(pair_lists)

    print(f"\nReflexive: {Reflexive}\n")
    
    

if __name__ == "__main__":
    main()
