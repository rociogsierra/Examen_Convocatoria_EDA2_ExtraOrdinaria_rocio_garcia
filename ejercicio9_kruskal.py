
#Generar un grafo no dirigido con planetas del MCU y diseñar los algoritmos necesarios para resolver las siguientes actividades

#clase nodo
class Node:
  def __init__(self, nombre):
    self.nombre = nombre
    self.vecino = {}   
  def agregar_nodo(self, nodo, peso):
    self.vecino[nodo] = peso

#clase grafo
class Grafo:
    
    #constructor de la clase
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
        self.padre = [i for i in range(vertices)]
        self.rango = [0 for i in range(vertices)]
        self.nombre_a_vertice = {}
        self.vertice_a_nombre = {}
    
    #agregar arista
    def agregar_arista(self, u, v, w):
        if u not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[u] = vertice
            self.vertice_a_nombre[vertice] = u
        if v not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[v] = vertice
            self.vertice_a_nombre[vertice] = v
        u = self.nombre_a_vertice[u]
        v = self.nombre_a_vertice[v]
        self.grafo.append((u, v, w))
    
    #encontrar
    def encontrar(self, i):
        if self.padre[i] == i:
            return i
        return self.encontrar(self.padre[i])
    
    #unir
    def unir(self, x, y):
        xroot = self.encontrar(x)
        yroot = self.encontrar(y)
        if self.rango[xroot] < self.rango[yroot]:
            self.padre[xroot] = yroot
        elif self.rango[xroot] > self.rango[yroot]:
            self.padre[yroot] = xroot
        else:
            self.padre[yroot] = xroot
            self.rango[xroot] += 1
    
    #Kruskal
    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda x: x[2])
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(u)
            y =self.encontrar(v)
            if x != y:
                e = e + 1
                resultado.append((u, v, w))
                self.unir(x, y)
        return resultado
    
    #obtener el peso del árbol
    def obtener_peso_arbol(self):
        arbol = self.kruskal()
        peso = 0
        for u, v, w in arbol:
            peso += w
        return peso

    #obtener árbol
    def obtener_arbol(self):
        arbol = self.kruskal()
        resultado = []
        for u, v, w in arbol:
            resultado.append((self.vertice_a_nombre[u], self.vertice_a_nombre[v], w))
        return resultado
    
def definitivo2():
    grafo = Grafo(5)
    #parte grafo -> Tierra
    grafo.agregar_arista("Tierra", "Vormir", 43)
    grafo.agregar_arista("Tierra", "Knowhere", 177)
    grafo.agregar_arista("Tierra", "Titan", 193)
    grafo.agregar_arista("Tierra", "Zen-Whoberi", 222)
    #parte grafo -> Vormir
    grafo.agregar_arista("Vormir", "Titan", 180)
    grafo.agregar_arista("Vormir", "Knowhere", 20)
    grafo.agregar_arista("Vorimr", "Zen-Whoberi", 1789)
    #parte grafo -> Vormir, Zen-Whoberi
    grafo.agregar_arista("Vormir", "Zen-Whoberi", 43)
    grafo.agregar_arista("Vormir", "Zen-Whoberi", 177)
    grafo.agregar_arista("Vormir", "Zen-Whoberi", 193)
    grafo.agregar_arista("Vormir", "Zen-Whoberi", 222)

    #árbol de expansión mínima
    arbol = grafo.obtener_arbol()
    for u, v, w in arbol:
        print(f"{u} - {v}: {w} distancia")
    peso = sum(borde[2] for borde in arbol)

    #peso del árbol de expansión mínima
    print(f"El peso mínimo del árbol de expansión es: {peso}")



    





