import graphviz as gv

#Clases
class ExpressionNode:
    def __init__(self, value="ε", left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def display(self):
        if(self.left == None and self.right == None):
            if type(self.value) == ExpressionNode:
                self.value.display()
            else:
                print(self.value)
        else:
            print(self.value)
            if(self.left != None):
                print("Left: ", end="")
                self.left.display()
            if(self.right != None):
                print("Right: ", end="")
                self.right.display()
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



non_symbols = ['+', '*', '.', '(', ')']
symbols=['a','b']

stack = [] 
#Funciones
def subDivide(regex: str):##Make an expression tree
    global stack
    if len(regex) == 0 or regex=="ε":
        return [ExpressionNode("ε")]
    for i in regex:
        # +
        if(i == "+"):
            left = ExpressionNode(stack.pop())
            stack.append(left)
            stack.append(i)
        # *
        elif(i == "*"):
            left = ExpressionNode(stack.pop())
            stack.append(ExpressionNode(i, left))
        # ()
        elif(i == "("):
            stack.append(".")
        # ()
        elif(i == "("):
            stack.append(i)
        elif(i == ")"):
            cont = 1
            for j in range(len(stack)-2, -1, -1):
                if(stack[j] == ")"):
                    cont += 1
                elif(stack[j] == "("):
                    cont -= 1
                if(cont == 0):
                    break
            left = subDivide(stack[j+1:-1])
            left=left[1:]
            stack = stack[:j]
            if(top(stack)=="+"):
                left = ExpressionNode(stack.pop(), left[0])
            stack.append(left[0])
        # a or b
        elif(i in symbols):
            if(top(stack) in symbols or type(top(stack)) == ExpressionNode):
                left = ExpressionNode(stack.pop())
                stack.append(ExpressionNode(".", left, ExpressionNode(i)))
            else:
                stack.append(ExpressionNode(i))
        
    print(stack)
    return stack

        
def top(stack: list):
    if(len(stack) == 0):
        return None
    return stack[-1]
    
states=0
def regexToEnfa(regex: ExpressionNode): 
    global states
    if(regex!=None):
        if(regex.value=="ε"):
            start=(NFAState("q"+str(states),False))
            states=states+1
            end=(NFAState("q"+str(states),True))
            states=states+1
            transitions=[{start.name:{end.name:"ε"}}]
            nfa=NFA(start,end,transitions)
            # nfa.display()
            return nfa
        else:
            if(type(regex.value)==ExpressionNode):
                regex=regex.value
            if(regex.value in symbols):
                start=(NFAState("q"+str(states),False))
                states=states+1
                end=(NFAState("q"+str(states),True))
                states=states+1
                transitions=[{start.name:{end.name:regex.value}}]
                nfa=NFA(start,end,transitions)
                # nfa.display()
                return nfa
            
            elif(regex.value=="*"):
                left=regexToEnfa(regex.left)
                ##Kleene
                start=NFAState("q"+str(states),False)
                states=states+1
                end=NFAState("q"+str(states),True)
                states=states+1
                transitions=[{start.name:{left.start.name:"ε",end.name:"ε"}},
                            {left.end.name:{end.name:"ε",left.start.name:"ε"}}]
                left.end.isFinal=False
                transitions=transitions+left.transitions
                nfa=NFA(start,end,transitions)
                # nfa.display()
                return nfa
            elif(regex.value=="."):
                left=regexToEnfa(regex.left)
                right=regexToEnfa(regex.right)
                ##Concat
                transitions=[{left.end.name:{right.start.name:"ε"}}]
                left.end.isFinal=False
                transitions=transitions+left.transitions+right.transitions
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
    return None
        
def enfaTonfa(enfa):
    pass


def main():
    i="a+b+ab"
    s=subDivide(i)
    s[0].display()
    enfa=regexToEnfa(s[0])
    enfa.display()
    
if __name__ == "__main__":
    main()