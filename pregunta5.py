
#Copio la clase artefactos valiosos (de dentro de la mochila de la pregunta anterior)

class ArtefactosValioso(object):
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.caducidad = caducidad
        print("la conserva se ha creado con exito")

    def __str__(self):
        return "ArtefactosValioso[peso=" + str(self.peso) + ", nombre=" + str(self.nombre) + ", precio=" + str(self.precio) + ", caducidad=" + self.caducidad + "]"

#Implementa una función recursiva llamada “hijo sin amor” 
def hijo_sin_amor(mochila, indice):
    
    #sacar los objetos de la mochila de a uno a la vez hasta encontrar un anillo de poder o que no queden más objetos en la mochila
    if (indice >= len(mochila)):
        return False, indice
        #aqui hemos llegado al final de la lista, por lo que no hemos encontrado el objeto. retornamos false y el numero de elementos que hemos recorrido
    
    #determinar si la mochila contiene un anillo de poder y cuantos objetos fueron necesarios sacar para encontrarlo    
    if mochila[indice].nombre == 'Anillo de poder':
        return True, indice
        #aquí el objeto actual es un anillo de poder, asi que retornamos true para indicar que lo hemo encontrado, asi como el numero de elementos que hemos recorrido

    else:
        indice += 1
        return hijo_sin_amor(mochila, indice)
        #aquí el objeto actual no es un anillo de poder, asi que incrementamos en 1 el numero de objetos recorridos y llamamos recursivamente a este metodo. en la siguiente ejecución, al haber incrementado el valor de 'indice', estaremos comprobando el objeto siguiente de la lista.
    
#Utilizar una lista para representar la mochila
artefacto1 = ArtefactosValioso(0.1, "Botella", 1, "2050/12/24")
artefacto2 = ArtefactosValioso(0.5, "Manta", 40, "2040/01/04")
artefacto3 = ArtefactosValioso(0.3, "Anillo de poder", 1000000, "2030/05/01")
artefacto4 = ArtefactosValioso(1.5, "Prismaticos", 200, "2029/07/12")
mochila = [artefacto1, artefacto2, artefacto3, artefacto4]

#llamamos al metodo usar_la_fuerza con dos parametros: la lista a recorrer, y el numero inicial de elementos recorridos
resultado = hijo_sin_amor(mochila, 0)
print("encontrado=" + str(resultado[0]) + ", elementos_recorridos=" + str(resultado[1] + 1) + "]")
