diccionario = {2000: 2, 300: 2, 100: 1}
diccionario1 = {3800: 2, 100: 5}


def cortes(diccionario):
    posicion = 1800
    for clave in diccionario:
        valor = diccionario[clave]
        largo = clave
        print(valor)
        print(clave)
        while valor > 0:
            posicion = posicion - largo
            if posicion < 0:
                print("posicion 0 recorrido: 0")
                largo = -posicion
                posicion = 1800
                print("posicion 1 recorrido: " + str(posicion))
            else:
                print("posicion 2 corte: " + str(posicion))
                largo = clave
                valor = valor - 1


cortes(diccionario1)
cortes(diccionario)
