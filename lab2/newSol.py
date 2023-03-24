import graphviz as gv
class ExpressionNode:
    def __init__(self, value="ε", left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
    def print(self):
        print(self.value)
        if self.left:
            print("Left: ", end="")
            self.left.print()
        if self.right:
            print("Right: ", end="")
            self.right.print()
class NFA:
    def __init__(self, start, end, transitions):
        self.start = start
        self.end = end
        self.transitions = transitions #Lista de diccionarios
    def display(self):
        #Graphviz
        g = gv.Digraph(format='pdf')
        for i in self.transitions:
            for j in i:
                for k in i[j]:
                    g.edge(j,k,label=i[j][k])
        g.view()
        

class NFAState:
    def __init__(self, name, isFinal):
        self.name = name
        self.isFinal = isFinal

def subDivide(regex: str):
    if(len(regex)==1):
        return ExpressionNode(regex)
    else:
        for i in regex:
            if(i=="("):
                cont=1
                for j in range(regex.index(i)+1,len(regex)):
                    if(regex[j]=="("):
                        cont+=1
                    elif(regex[j]==")"):
                        cont-=1
                    if(cont==0):
                        break
                if(regex[regex.index(i)+1]=="*"):
                    left=ExpressionNode("*",subDivide(regex[regex.index(i)+2:j]))
                    right=subDivide(regex[j+1:])
                    return ExpressionNode("()",left,right)
                else:
                    left=subDivide(regex[regex.index(i)+1:j])
                    right=subDivide(regex[j+1:])
                    return ExpressionNode("()",left,right)
            elif(i=="+"):
                left=subDivide(regex[:regex.index(i)])
                right=subDivide(regex[regex.index(i)+1:])
                ##Change if left or right are none
                return ExpressionNode(i,left,right)
            elif(onlyInAlphabet(regex)):
                left=ExpressionNode(regex[0])
                right=subDivide(regex[1:])
                return ExpressionNode(".",left,right)
            
def onlyInAlphabet(regex: str):
    for i in regex:
        if(i!="a" and i!="b"):
            return False
    return True
states=0
def regexToEnfa(regex: ExpressionNode): 
    ##Create another tree with NFA nodes that parce the regex tree
    ##Create a graph with the NFA nodes
    ##Return the graph
    global states
    if(regex!=None):
        if(regex.value=="a" or regex.value=="b"):
            start=NFAState("q"+str(states),False)
            states=states+1
            end=NFAState("q"+str(states),True)
            states=states+1            
            transitions=[{start.name:{end.name:regex.value}}]
            nfa=NFA(start,end,transitions)
            # nfa.display()
            return nfa
        # elif(regex.value=="*"):
        #     left=regexToEnfa(regex.left)
        #     ##Kleene
        #     start=NFAState("q"+str(states),False)
        #     states=states+1
        #     end=NFAState("q"+str(states),True)
        #     states=states+1
        #     transitions=[{start.name:{left.start.name:"ε",end.name:"ε"}},
        #                 {left.end.name:{left.start.name:"ε",end.name:"ε"}}]
        #     left.end.isFinal=False
        #     return nfa
        elif(regex.value=="."):
            left=regexToEnfa(regex.left)
            right=regexToEnfa(regex.right)
            ##Concatenate
            left.end.isFinal=False
            transitions=left.transitions
            transitions.append({left.end.name:{right.start.name:"ε"}})
            transitions=transitions+right.transitions
            nfa=NFA(left.start,right.end,transitions)
            # nfa.display()
            return nfa
        elif(regex.value=="+"):
            left=regexToEnfa(regex.left)
            right=regexToEnfa(regex.right)
            ##Union
            start=NFAState("q"+str(states),False)
            states=states+1
            end=NFAState("q"+str(states),True)
            states=states+1
            transitions=[{start.name:{left.start.name:"ε",right.start.name:"ε"}},
                        {left.end.name:{end.name:"ε"}},
                        {right.end.name:{end.name:"ε"}}]
            left.end.isFinal=False
            right.end.isFinal=False
            transitions=transitions+left.transitions+right.transitions
            nfa=NFA(start,end,transitions)
            # nfa.display()
            return nfa
        elif(regex.value=="()"):
            left=regexToEnfa(regex.left)
            right=regexToEnfa(regex.right)
            if(left==None):
                return right
            elif(right==None):
                return left
            else:
                left.end.isFinal=False
                transitions=left.transitions
                transitions.append({left.end.name:{right.start.name:"ε"}})
                transitions=transitions+right.transitions
                nfa=NFA(left.start,right.end,transitions,states)
                # nfa.display()
            return nfa
    return None
        
def enfaTonfa(enfa):
    pass

def main():
    i="(a+b)+(ab)"
    s=subDivide(i)
    s.print()
    enfa=regexToEnfa(s)
    enfa.display()
    nfa=enfaTonfa(enfa)
    
if __name__ == "__main__":
    main()
