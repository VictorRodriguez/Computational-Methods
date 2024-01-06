import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(val):
    """
    Here goes your code to do the analysis
    1. Reflexive: aRa for all a in X,
    2. Symmetric: aRb implies bRa for all a,b in X
    3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    """
    Reflexive = False
    Symmetric = False
    Transitive = False

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
    g = graphviz.Digraph('G', filename='hello.gv')
    g.edges(stringListEdges)
    g.view()

def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    alphabet = getAlphabet(val)
    plotList = formatInput(val)
    print(plotList)
    print(alphabet)
    Reflexive,Symmetric,Transitive = analyze(plotList)
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(plotList)

if __name__ == "__main__":
    main()
