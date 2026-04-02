### Exception Handling ###

number_one = 5
# number_two = 1
number_two = "1"

# --- Excepción base: try except ---

# print(number_one + number_two) Genera un error

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

# --- Flujo completo de una excepción: try except else finally ---

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta su no se produce una excepción
    print("La ejecución  continpua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# --- Excepciones por tipo ---

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# --- Captura de la información de la excepción ---

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError as error:
    print("error")
except Exception as error:
    print(error)