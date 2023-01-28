
#Creación
#Crea una clase llamada artefactosvaliosos.py que tenga los atributos peso, nombre, precio y fecha de caducidad

class ArtefactosValioso(object):
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.caducidad = caducidad
        
        #Crea el constructor de la clase. Añade en el constructor un print para informar de que la conserva se ha creado con éxito
        print("conserva creada con exito")
        
        #Crea el método __str__ para visualizar por pantalla la información de los productos
        def __str__(self):
            return "ArtefactosValioso[peso=" + str(self.peso) + ", nombre=" + str(self.nombre) + ", precio=" + str(self.precio) + ", caducidad=" + self.caducidad + "]"

#Experimentación
#Crea algunos artefactos valiosos
artefacto1 = ArtefactosValioso(5.0, "Diamante", 60000, "2050/12/24")
artefacto2 = ArtefactosValioso(0.2, "Reloj", 700, "2030/05/01")
artefacto3 = ArtefactosValioso(1200, "Coche", 50000, "2040/01/04")

#Prueba a mostrar los datos de algunos artefactos valiosos ordenados por su fecha de caducidad y a modificar algún valor, por ejemplo, prueba a modificar el precio de un de la conserva
artefactos_ordenados = sorted(artefactos, key=lambda x: x.caducidad)
for artefacto in artefactos_ordenados:
    print(artefacto.nombre)
#añado esto para ver como se puede modificar un atributo de la clase y luego lo printo para demostrar que su precio ha cambiado
artefacto2.precio = 800
print(artefacto2)
