
from random import randrange

#Deberá generar 2000 Armaduras siguiendo el formato de la imagen del primer ejercicio contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;
LEGIONES = ["FL", "TF", "TK", "CT", "FN", "FO"]
NUM_ARMADURAS = 2000

#deberá cargar los Armaduras generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo con los tres últimos dígitos del código y en la segunda a partir de las iniciales de la legión
class armaduras(object):
    def __init__(self):
        self.cal = None
        print("Stormtrooper creado con exito")

    def calificacion(self, codigo, digitos):
        self.codigo = codigo
        self.digitos = digitos
        self.cal = self.codigo + "-" + str(self.digitos)
    
    #tabla hash legion
    def hash_legion(self):
        return self.codigo
    #tabla hash digitos
    def hash_digitos(self):
        return self.digitos % 1000

    def __str__(self):
        return self.cal  

#creación tablas hash  
class HashTale(object):

    def __init__(self, keys):
        self.table = {}
        for key in keys:
            self.table[key] = []

    def get(self, key):
        if key in self.table.keys():
            return self.table[key]
        else:
            return []

    def insert(self, key, value):
        if key in self.table.keys():
            self.table[key].append(value)

    def remove(self, key, value):
        if key in self.table.keys():
            if value in self.table[key]:
                self.table[key].remove(value)
                print("Elemento borrado: " + str(value))
            else:
                print("Elemento no encontrado; " + str(value))

    def __str__(self):
        result = "HashTable[\n"
        for key,values in self.table.items():
            result = result + str(key) + " -> "
            for value in values:
                result = result + str(value) + ","
            if (len(values)) > 0:
                result = result[:len(result)-1] # we remove the last ","
            result += "\n"
        result += "]"
        return result

def generar_codigo():
    return LEGIONES[randrange(len(LEGIONES))]
def generar_digitos():
    return randrange(100000)
lista_indices = list(range(0, 1000))

#generar armaduras y construir tablas
legion_table = HashTale(LEGIONES)
codigo_table = HashTale(lista_indices)

for i in range(NUM_TROOPERS):
    # creamos la armadura con calificacion "aletaoria"
    legion = generar_codigo()
    digitos = generar_digitos()
    soldado = armaduras()
    soldado.calificacion(legion, digitos)
    #insertamos en la tabla de hash
    hash_legion = soldado.hash_legion()
    hash_digitos = soldado.hash_digitos()
    legion_table.insert(hash_legion, soldado)
    codigo_table.insert(hash_digitos, soldado)

print(legion_table)
print("\n\n\n")
print(codigo_table)

#determinar si el Armaduras FN-2187 está cargado para poder quitarlo porque es un trai dor desertor.
desertor = Stormtrooper()
desertor.calificacion("FN", 2187)
legion_table.remove(desertor.hash_legion(), desertor)
codigo_table.remove(desertor.hash_digitos(), desertor)

mision_asalto = codigo_table.get(781)
mision_exploracion = codigo_table.get(537)

#ahora obtenga todos los Armaduras terminados en 781 para asignarlos a una misión de asalto y a los terminados en 537 para una misión de exploración
#Asignacion a mision de exploracion en hoth y exterminacion a Endor
mision_exploracion_hoth = legion_table.get("CT")
print("Mision de exploracion en Hoth: ")
for soldado in mision_exploracion_hoth:
    print(str(soldado))
print("\n")

mision_asalto_endor = legion_table.get("TF")
print("Mision de asalto en Endor: ")
for soldado in mision_asalto_endor:
    print(str(soldado))
print("\n")

