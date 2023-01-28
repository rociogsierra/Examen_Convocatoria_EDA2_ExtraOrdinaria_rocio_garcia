
#Creación
class object():
    def __init__(self, codigo, cohoerte, siglo, escuadra, armadura):
        self.codigo = codigo
        self.cohoerte = cohoerte
        self.siglo = siglo
        self.escuadra =escuadra
        self.armadura = armadura

#Crea una clase llamada armaduras.py que tenga los atributos nombre y rango
class armaduras(object):
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        
        #Crea el constructor de la clase. Añadir en el constructor un print para informar de que la armadura se ha creado con éxito.
        print("la armadura se ha creado con éxito")
    
    #Crear un método llamado calificacion que clasifique a las armaduras de IronMan
    def calificacion(self):
        codigo_legion = self.codigo
        id_cohoerte = self.cohoerte
        id_siglo = self.siglo
        id_escuadra = self.escuadra
        numero_armadura = self.armadura
        return codigo_legion + "-" + str(id_cohoerte) + str(id_siglo) + str(id_escuadra) + str(numero_armadura)

#Experimentación
#Crea una lista con un numero arbitrario de objetos tipo armaduras
armadura1 = armaduras("armadura 1", "escudo")
armadura2 = armaduras("armadura 2", "espada")
armadura3 = armaduras("armadura 3", "coraza")
armas = [armadura1, armadura2, armadura3]

#Recorre los elementos de la lista, y prueba a ejecutar el método calificación de cada objeto que has creado
for arma in armas:
    cal = arma.calificacion("MK", 8, 8, 8, 8)
    print(cal)