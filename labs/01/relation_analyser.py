# Sergio Alfonso Casillas Santoyo A01424863

def generar_script_graphviz(pares):
    script = "digraph ejemplo {\n\n\trankdir=LR;\n\tnode [shape = circle];\n"
    for x, y in pares:
        script += f"\t{x} -> {y} ;\n"
    script += "\n}"
    return script

def es_reflexivo(pares, elementos):
    return all((e, e) in pares for e in elementos)

def es_simetrico(pares):
    return all((y, x) in pares for x, y in pares)

def es_transitivo(pares):
    for x, y in pares:
        for _, z in pares:
            if (y, z) in pares and (x, z) not in pares:
                return False
    return True


pares = {(0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3)}


elementos = set(x for x, _ in pares).union(y for _, y in pares)


reflexivo = es_reflexivo(pares, elementos)
simetrico = es_simetrico(pares)
transitivo = es_transitivo(pares)
equivalencia = reflexivo and simetrico and transitivo


print(f"(a) R es reflexiva: {'Sí' if reflexivo else 'No'}")
print(f"(b) R es simétrica: {'Sí' if simetrico else 'No'}")
print(f"(c) R no es transitiva: {'No' if transitivo else 'Sí'}")
print(f"(d) R no tiene relación de equivalencia: {'No' if equivalencia else 'Sí'}")


script_graphviz = generar_script_graphviz(pares)


ruta_archivo_graph_log = r'C:\Users\dripl\OneDrive\Escritorio\Programacion universidad invierno\graph.log'


with open(ruta_archivo_graph_log, 'w') as archivo:
    archivo.write(script_graphviz)
