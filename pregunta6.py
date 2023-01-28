
precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100

#¿Cuál es el valor máximo de los artículos que se pueden agregar a la mochila de manera que el peso no exceda el límite de peso W?
def calcular_maximo(precios, pesos, peso_maximo):
    longitud = len(precio)
    
    #creamos una tabla (2 dimensiones) de longitud 6x101
    tabla = [[0 for x in range(peso_maximo + 1)] for x in range(longitud + 1)]

    #relleno la tabla por filas, finalizando primero cada columna de la fila
    for i in range(longitud + 1):
        for j in range(peso_maximo + 1):
            #la primera fila y columna siempre sera el valor 0, pues indica que no hemos metido ningun objeto en la mochila.
            if i == 0 or j == 0:
                tabla[i][j] = 0
            #el objeto actual cabe en la mochila. se calcula el valor que supondria añadirlo
            elif pesos[i - 1] <= j:
                tabla[i][j] = max(precios[i - 1] + tabla[i - 1][j - pesos[i - 1]], tabla[i - 1][j])
                # el objeto actual supera el limite (j), asi que no lo metemos en la mochila,y  comprobaremos el siguiente objeto en la siguiente iteracion
            else:
                tabla[i][j] = tabla[i - 1][j]
            
            #devolvemos la ultima posición de la tabla (ultima fila y ultima columna), pues despues de los calculos tendra el valor maximo posible sin haber soprepasado el limite
        return tabla[longitud][peso_maximo]

#SOLUCIÓN
valor_maximo = calcular_maximo(precio, pesos, peso_maximo)
print("El valor maximo es " + str(valor_maximo))
