
import sys

#clase grafo
class Grafo:
    #constructor del grafo
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.distancias = {}
    
    #agregar nodos
    def agregar_nodo(self, valor):
        self.nodos.add(valor)
    
    #agregar aristas
    def agregar_arista(self, nodo_origen, nodo_destino, distancia):
        if nodo_origen not in self.aristas:
            self.aristas[nodo_origen] = [nodo_destino]
        else:
            self.aristas[nodo_origen].append(nodo_destino)
        if nodo_destino not in self.aristas:
            self.aristas[nodo_destino] = [nodo_origen]
        else:
            self.aristas[nodo_destino].append(nodo_origen)
        self.distancias[(nodo_origen, nodo_destino)] = distancia
        self.distancias[(nodo_destino, nodo_origen)] = distancia

    #definición djkistra
    def dijkstra(self, inicio, fin):
        
        #diccionario de nodos
        rutas_mas_cortas = {inicio: (None, 0)}
        nodo_actual = inicio
        visitados = set()

        while nodo_actual != fin:
            visitados.add(nodo_actual)
            destinos = self.aristas[nodo_actual]
            peso_al_nodo_actual = rutas_mas_cortas[nodo_actual][1]

            for siguiente_nodo in destinos:
                peso = self.distancias[(nodo_actual, siguiente_nodo)] + peso_al_nodo_actual
                if siguiente_nodo not in rutas_mas_cortas:
                    rutas_mas_cortas[siguiente_nodo] = (nodo_actual, peso)
                else:
                    peso_actual_mas_corto = rutas_mas_cortas[siguiente_nodo][1]
                    if peso_actual_mas_corto > peso:
                        rutas_mas_cortas[siguiente_nodo] = (nodo_actual, peso)
            
            siguientes_destinos = {nodo: rutas_mas_cortas[nodo] for nodo in rutas_mas_cortas if nodo not in visitados}
            if not siguientes_destinos:
                return "Ruta No Posible"
                #destino con el menor peso
            nodo_actual = min(siguientes_destinos, key=lambda k: siguientes_destinos[k][1])

        #lista ruta
        ruta = []
        while nodo_actual is not None:
            ruta.append(nodo_actual)
            siguiente_nodo = rutas_mas_cortas[nodo_actual][0]
            nodo_actual = siguiente_nodo
        #lista ruta inversa
        ruta = ruta[::-1]

        #pesos de las aristas
        for i in range(len(ruta) - 1):
            print(f"{ruta[i]} -> {ruta[i+1]}: {self.distancias[(ruta[i], ruta[i+1])]}")
        
        #costo final de la ruta + ruta más corta
        return ruta, rutas_mas_cortas[fin][1]

#grafo definitivo

def definitivo():    
    grafo = Grafo()
    planetas = ["Tierra", "Knowhere", "Zen-Whoberi", "Vomir", "Titán", "Nidavellir"]
    for planeta in planetas:
        grafo.agregar_nodo(planetas)
    
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

#Llamamos a la funcion dijkstra para encontrar el camino critico mas corto
    ruta_mas_corta1, peso = grafo.dijkstra("Tierra", "Vormir")
    ruta_mas_corta2, peso2 = grafo.dijkstra("Knowhere","Titán")
    ruta_mas_corta3, peso3 = grafo.dijkstra("Zen-Whoberi","NidaVellir")
    print(ruta_mas_corta1)
    print(ruta_mas_corta2)
    print(ruta_mas_corta3)


            