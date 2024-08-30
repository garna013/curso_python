### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta solo si hay una excepcion
    print("Se ha producido un error")
    
# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce un excepcion
    print("La ejecucion continua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecucion continua")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as e:
    print(e)
except Exception as exceptionerror:
    print(exceptionerror)

