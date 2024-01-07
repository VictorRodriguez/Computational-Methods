import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def transitiveCheck(lista):
    for i in range(0,len(lista)-1):
        if lista[i][0] != lista[i][1]:
            inReferenceA = lista[i]
            print("A",inReferenceA)
            """for j in range(0,len(lista)-1):
                if inReferenceA[1] == lista[j][0] and lista[j][0] != lista[j][1] and lista[j] != inReferenceA:
                    inReferenceB = lista[j]
                    print("B",inReferenceB)
                    for k in range(0,len(lista)-1):
                        if lista[k][0] == inReferenceB[1] and lista[k][1] == inReferenceA[0] and lista[k][0] != lista[k][1] and lista[k] != inReferenceB and lista[k] != inReferenceA:
                            inReferenceC = lista[k]
                            print("C", inReferenceC , "\n")"""

def similaritiesInLists(a,b):
    return [i for i, j in zip(a, b) if i == j]

def reverseStringinList(list):
	newList = []
	for i in range(0,len(list)):
		newList.append(list[i][::-1])
	return newList

def analyze(val, alphabet):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    reflexiveCheckboxes = [False] * len(alphabet)
    symmetricCheckboxes = [False] * len(alphabet)
    transitiveCheckboxes = [False] * len(alphabet)

    
    Reflexive = False
    Symmetric = False
    Transitive = False
    
    for i in range(0,len(val)-1):
        if val[i][0] == val[i][1]:
            Reflexive = True
	        #reflexiveCheckboxes[int(val[i][0])] = True
	        
    reverseList = reverseStringinList(val)
    
    
    if len(similaritiesInLists(val,reverseList)) != 0:
        Symmetric = True
    
    transitiveCheck(val)
		

    return Reflexive,Symmetric,Transitive
    

def formatInput(stringInput):
	n = 2
	initStr = ''.join(char for char in stringInput if char.isdigit())
	fList = [initStr[i:i+n] for i in range(0, len(initStr), n)]
	return fList
    
def getAlphabet(fDescriptionString):
	numeric_set = {int(char) for char in fDescriptionString if char.isdigit()}
	return numeric_set
	
def plot(stringListEdges):
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph('G', filename='graphOutput.gv')
    g.edges(stringListEdges)
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    alphabet = getAlphabet(val)
    plotList = formatInput(val)
    print(plotList, "\n")
    print(alphabet, "\n")
    Reflexive,Symmetric,Transitive = analyze(plotList,alphabet)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(plotList)

if __name__ == "__main__":
    main()
