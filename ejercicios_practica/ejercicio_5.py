# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n')) # -2
fin = int(input('Ingrese el último número de la secuencia\n'))    #  5
sumatoria = 0  # Inicializo el contador en 0

range ((inicio), (fin))


# for ... in range(....)

print ('los numeros incluidos en la secuencia son:')
for i in range ((inicio), (fin)):
    print (inicio)
    sumatoria += i

# Imprimir el valor de la sumatoria

print("El valor de sumatoria es:", sumatoria)


print("terminamos!")
