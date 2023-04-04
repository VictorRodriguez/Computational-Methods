#LAB 02 -- A01566927

# IMPORTANTE
  # OR == "U"
  # RECURSION == "*"
  # Los regex deben de estar dentro de un parentesis, por ejemplo (01) o (abUb)(a)

#LIBRERIAS
import re
from collections import defaultdict
import graphviz

#---CASOS PRUEBA DE VALIDACION---

regex="(abUa)*"
#regex="(01U0)*"
#regex= "(01)(000)(1)"
#regex="(aUaba)*"
#regex="(abUa)"
#regex="(abab)"
#regex="(abab)(a)"

#---VALIDAR REGEX---
# Si se ingresa un simbolo que no sea parte del alfabeto o los operandos, no se acepta el REGEX

if(re.search(r'[^ab10E()*U]+',regex)!=None):
  #Regex inválido, se termina
  print("INVALID REGEX")
  
else:
  print("VALID REGEX")

  #---PASO 0---
  #Creamos Grafo
  graph=graphviz.Digraph('G', filename='Lab_02')
  graph.attr(rankdir='LR')
  graph.attr('node', shape='circle')

  #NODOS
  n=0
  nodes=defaultdict(list)

  #---PASO 1---
  #Separar por bloques de parentesis
  step_01=re.findall(r'\([\w]*\)\*?',regex)

  #---PASO 2---
  #Separar por caracter y por simbolos
  for operation in step_01:
    step_02=re.findall(r'[ab01E]|[U*]',operation)

    symbols=re.findall(r'[ab01E]+',operation)

    #Creamos concatenaciones
    for symbol in symbols:
      for i in range(len(symbol)):
        nodes[n]=[n+1]
        graph.edge(str(n),str(n+1), label=str(symbol[i]))
        n+=1
      n+=1

    #---PASO 3---
    #Crear restricciones 
    for i in range(len(step_02)):
      #Crear union
      #Creamos dos estados extra, uno al inicio y otro al final, 
      # llevando al mismo camino cual sea la opcion
      if (step_02[i]=="U"):

        graph.node(str(n), shape='doublecircle')
        graph.edge(str(i),str(n), label="E")
        graph.edge(str(n-1),str(n), label=str("E"))

        graph.edge(str(n+1),str(i+1), label=str("E"))
        graph.edge(str(n+1),str(0), label=str("E"))
        
        nodes[i].append(n)
        nodes[n-1].append(n)
        nodes[n+1].append(i+1)
        nodes[n+1].append(0)
        n+=1

      #Creamos recursividad
      #Unimos el nodo inicial y el final con un E para hacer un ciclo
      # ademas de definir los dos estados de aceptacion
      elif (step_02[i]=="*"):
        if("U" not in step_02):
          graph.edge(str(0),str(n), label=str("E"))
          graph.edge(str(n),str(0), label=str("E"))
        else:
          graph.node(str(n), shape='doublecircle')
          graph.edge(str(n),str(n-1), label=str("E"))
          graph.edge(str(n-1),str(n), label=str("E"))
          graph.node(str(len(nodes)), shape='doublecircle')
          
          nodes[n].append(n-1)
          nodes[n-1].append(n)

    #Restriccion para unir parentesis en caso de que haya mas de un parentesis 
    if ((len(step_01))>1):
      graph.edge(str(n-1),str(n), label=str("E"))

  #Restriccion para que puedan haber uniones dentro de un solo parentesis
  if ((len(step_01))<2 and "U" not in step_02):
    graph.edge(str(n-1),str(n), label=str("E"))

  #Restriccion para crear estado de aceptacion en caso de que no haya union o recursividad
  if("U" not in step_02 and "*" not in step_02):
    graph.node(str(n), shape='doublecircle')

  #Generar grafo
  graph.view()
