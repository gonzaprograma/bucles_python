# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Realizar un bucle "while" cuya condición de continuidad
# sea que <x sea menor a 10> y que <x sea distinto de 6>
# Colocar ambas condiciones como condicion del "while" realizando
# una condición compuesta (utilice el operador "and" o "or" según corresponda)
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

while x < 10 and x != 6:
    x += 2
    print ('el valor de x=', x)
else:
    print ('el valor de x no cumple la condicion de continuidad al ser x = 6')

# Realice el mismo bucle "while" pero en vez de estar formado por una condición
# compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
# "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
# En cada iteracion del bucle debe incrementar el valor de "x" en "2"
# e imprimir en pantalla el resultado de X (antes de incrementar) con print

x = int(input()) #probar con x = 0 y siendo x = 1 para ver distinto resultados

while x < 10:
    x += 2
    print ('el valor de x =', x)
    if x == 6:
        break
    
print ('el bucle finalizó ya que x es igual a 6 o es mayor a 10')


print("terminamos!")