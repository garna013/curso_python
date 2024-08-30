### Operadores Aritmeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)   # El % te coge el resto de una division
print(10 // 3)  # Numero entero de de una division aproximada
print(2 ** 3)   # Exponentes 2 elevado a 3

print("Hola " + "Python " +"¿Que tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (5 - 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))
 
 
 
### Operadores Comparativos ###
 
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)


print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")                 # Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa"))       # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")



### Operadores Comparativos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 > 4 or "Hola" < "Python")
print(3 > 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 > 4) and "Hola" < "Python")