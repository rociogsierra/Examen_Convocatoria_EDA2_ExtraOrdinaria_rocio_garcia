
#este ejercicio lo tenía medio resuelto en uno de mis repositorios de tablas hash
#clase nodo arbol
class nodo_arbol(object): 
    def __init__(self, izquierda=None, derecha=None):
        self.izq = izquierda
        self.der = derecha
    def children(self):
        return self.izq, self.der
    def __str__(self):
        return self.izq, self.der

#árbol de hauffman
def huffman_arbol_code(nodo, binString=''):
    if type(nodo) is str:
        return {nodo: binString}
    (l, r) = nodo.children()
    d = dict()
    d.update(huffman_arbol_code(l, binString + '0'))
    d.update(huffman_arbol_code(r, binString + '1'))
    return d

#descodificar árbol de hauffman
def huffman_arbol_decode(message, nodo_raiz, nodo, msgd=''):
    if len(message) == 0:
        print("descodificado: {}".format(msgd))
        return msgd
    if type(nodo) is str:
        msgd = msgd + nodo
        nodo = nodo_raiz
    (l, r) = nodo.children()
    caracter = message[0]

    if len(message) == 1:
        message = ''
    else:
        message = message[1:]

    if caracter == '1':
        huffman_arbol_decode(message, nodo_raiz, r, msgd=msgd)
    else:
        huffman_arbol_decode(message, nodo_raiz, l, msgd=msgd)

#crear árbol de hauffman definitivo
def creararbol(nodos):
    print(nodos)
    print('\n')
    while len(nodos) > 1:
        (key1, c1) = nodos[0]
        (key2, c2) = nodos[1]
        nodos = nodos[2:]
        nodo = nodo_arbol(key1, key2)
        nodos.append((nodo, c1 + c2))
        nodos = sorted(nodos, key=lambda x: x[1], reverse=False)
        print(nodos)
        print('\n')
    return nodos[0][0]

#creación de la tabla propuesta en el enunciado
tabla = {
    'A': 0.2,
    'F': 0.17,
    '1': 0.13,
    '3': 0.21,
    '0': 0.05,
    'M': 0.09,
    'T': 0.15
}

tabla = sorted(tabla.items(), key=lambda x: x[1], reverse=False)
arbol = creararbol(tabla)
encoded = huffman_arbol_code(arbol)
for i in encoded:
    print(i + " : " + encoded[i])

mensaje = '1110101110101000100111'
# deberia printar F33T0A1
huffman_arbol_decode(mensaje, arbol, arbol)


