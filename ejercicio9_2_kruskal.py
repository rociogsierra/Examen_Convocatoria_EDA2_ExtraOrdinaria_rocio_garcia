
import sys

#clase grafo
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.distancias = {}

    def agregar_nodo(self, valor):
        self.nodos.add(valor)

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

    def dijkstra(self, inicio, fin):
        #rutas_mas_cortas es un diccionario de nodos
        #que tiene por valor una tupla de (nodo previo, peso)
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
                # el siguiente nodo es el destino con el menor peso
            nodo_actual = min(siguientes_destinos, key=lambda k: siguientes_destinos[k][1])
            
            