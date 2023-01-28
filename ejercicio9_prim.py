
from intertools import permutations

#función del árbol de mínima expansión
def MinimumSpanningTree(grafo, s, planetas):
    vertex = []
    
    for i in range(V):
        if i != s:
            vertex.append(i)
    final_path = []
    min_path = 10000000
    next_permutation = permutations(vertex)
    
    for i in next_permutation:
        current_pathweight = 0 
        k = s
        current_path = []
        
        for j in i:
            current_pathweight += grafo[k][j]
            curent_path.append('{}-->{}'.format(dict_of_planets[k],dict_of_planets[j]))
            k = j
        current_pathweight += grafo[k][s]
        current_path.append('{}-->{}'.format(dict_of_planets[k],dict_of_planets[s]))
        
        if current_pathweight < min_path:
            final_path = current_path
            min_path = current_pathweight
        
    return min_path, final_path

#planetas: Tierra, Knowhere, Zen-Whoberi, Vomir, Titán, Nidavellir, agregue 7 más
dict_of_panets = {
    0:'Tierra',
    1:'Knowhere',
    2:'Zen-Whoberi',
    3:'Vomir',
    4:'Titán',
    5:'Nidavellir',
    6:'Agregado1',
    7:'Agregado2',
    8:'Agregado3',
    9:'Agregado4',
    10:'Agregado5',
    11:'Agregado6',
    12:'Agregado7',
}

#Determinar el costo mínimo posible para el camino (del árbol de mínima expansión)
final_cost, path = solver(graph, s, nombres_superheroes)
print('El mínimo costo posible es: {} para el camino {}'.format(final_cost, path))

#generacion de aristas (tiene que haber 4)
class Nodoarista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None
class Nodovertice(object):
    def __init__(self, info):
        self.info = info
        self.sig - None
        self.visitado = False
        self.adyacentes - Arista()

#creación del grafo
class grafo(object):
    def __init__(self, dirigido = True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

#creacion de aristas
class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
def insertar_vertice(grafo, dato):
    nodo = Nodovertice(dato)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1   

#insertar aristas
def insertar_arista(grafo, dato, origen, destino):
    agregar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregar_arista(destino.adyacentes, dato, origen.info)
def agregar_arista(origen, dato, destino):
    nodo = Nodoarista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo = Nodoarista(dato, destino)
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

#para conectar unos planetas con otros
print('\nPunto d')
for ind, vecino in enumerate(grafo[3]):
	if vecino != 0:
		print('Tatooine se puede conectar con {}'.format(dict_of_planets[ind]))
        