#Stefano Herrejon Antuñano
#A000571720

#Programa para leer un string y decir si es reflexive, symmetric, transitive y/o equivalence relation

#Variables universales
list = []
listA = []
reflex = False
symm = False
trans = False


#Inputs
x = input()
#y = "{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3),(1,3),(3,1) }"

#FUNCIONES----

#Lectura y almacenaje 
#Lee el string(input), en caso de ser numero lo guarda y cuando llega una coma o llave para cerrar lo agrega a una lista como int
#En caso de que sea el primer numero con ese valor se guarda en listA
def lectura(rawNums):
    eje = ""
    for x in rawNums:
        if x != "(" and x != ")" and x != "{" and x != "}"and x != "," and x != " ":
       # if x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "0" :
            eje = eje+x
        if x =="," or x == "}":
            list.append(str(eje))
            if not str(eje) in listA:
                listA.append(str(eje))
            eje=""
    

#reflexive
#Se crea una lista boleana (False) para cada valor no repetido, se recorre la list para comparar si hay 2 valores seguidos identicos 
# (que sea reflexive). En caso de que sean el lugar correspondiente al dato en la lista boleana bol se vuelve True 
# Si hay un False al final la lista no es reflexive, en caso contrario lo es

def reflexive():
    bol =  [False for i in range(len(listA))]

    for x in range (0,len(list),2):
        if(list[x] == list[x+1]):
            bol[listA.index(list[x])] = True

    if False in bol:
        print("(a) R is NOT reflexive,")
    else :
        print("(a) R is reflexive,")
        global reflex
        reflex = True
    

#symmetric
#Se crea una lista boleana (False)
#En caso de que sean reflexive se marca como True
#Si no se busca que 


def symmetric():

    bol =  [False for i in range(len(list))]

    for x in range (0,len(list),2):
        if(list[x] == list[x+1]):
            bol[x] = True
            bol[x+1] = True
        else:
            for y in range(x,len(list),2):
                if(list[x] == list[y+1] and list[x+1] == list[y]):
                    bol[x] = True
                    bol[x+1] = True
                    bol[y] = True
                    bol[y+1] = True

    if False in bol:
        print("(b) R is NOT symmetric,")
    else :
        print("(b) R is symmetric,")
        global symm
        symm = True


#transitive
#Triple ciclo para poder identificar cuando x->y, y->z que halla x->z

def transitive():
    bandera = False

    for x in range(0,len(list),2):
        #print("x : ",list[x]," ",list[x+1])
        if (list[x] == list[x+1]):
            continue
       
        #print(" -> Y")
        for y in range(0,len(list),2):
           # print("y : ",list[y]," ",list[y+1])
            if(list[x+1] == list[y] and list[x] != list[y+1] and list[y] != list[y+1]):
                #print("<-> Z")
            
                for z in range(0,len(list),2):
                    
                    #print("Z :",list[z]," ",list[z+1])

                    if (list[x] == list[z] and list[z+1] == list[y+1]):
                        bandera = True
                        #print("TRUE")
                        break
                    else :
                        bandera = False
        #print("-----")

    if (bandera == True):
        print("(c) R is transitive.")
        global trans
        trans = True

    else :
        print("(c) R is NOT transitive,")



#equivalence
#En caso de que las banderas para reflexive, symmetric y transitive son True y el tamaño de la lista es mayor a 1 es eqyuvalence

def equivalence():
    if(len(list) >= 1 and reflex == True and symm == True and trans == True):
        print("(d) R does have equivalence relation")
    else :
        print("(d) R does NOT have equivalence relation")


#graph
#Se crea el archivo graph.log para ponerlo en https://dreampuf.github.io/GraphvizOnline/

def graph():
    f = open("graph.log","w")
    f.write("digraph G {\n rankdir=LR;\n node [shape = circle];\n")
    for x in range(0,len(list),2):
        relacion = list[x]+"->"+list[x+1]
        f.write(relacion+"\n")
    f.write("}\n")
    f.close()

#Llama a las funciones

#{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3),(1,3),(3,1) } = R,S,T
#{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (1,3),(3,1) } = S,T
#{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (1,3),(3,1) }
#{ (a,a), (a,b), (a,d), (b,a), (b,b), (c,c), (d,a), (d,d),(b,d),(d,b) }
    
lectura(x)
reflexive()
symmetric()
transitive()
equivalence()
graph()
print(list)
print("-12345-")
print(listA)
