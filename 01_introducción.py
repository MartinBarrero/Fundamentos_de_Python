# Hello World -> Esto es un comentario

"""
Esto es un bloque de comentario
Puede trabajarse en varias lineas
"""

'''
Y también se pude manejar
de esta manera
'''

print("Hello World")

# Operaciones adicionales (aparte de las básicas)
print (5 ** 2)  # Potencia
print (3 % 2)   # Modulo
print (3 // 2)  # Floor division

# Consultar y conocer diferentes tipos de datos
print(type("Hello World"))                       # String
print(type(5))                                   # int
print(type(0.5))                                 # float
print(type([0 , 11 , 5 , 58]))                   # List
print(type({"name": "Martín" , "ID": "123"}))    # Dictionary
print(type({1.5, 3.14, 2.7}))                    # Set
print(type((1.5 , 3.14 , 2.7)))                  # Tuple
print(type(True))                                # bool
print(type(None))                                # None

"""
Apuntes Datos Agrupados

    1. List -> Vector (similar no igual)

    2. Dict -> Clave: Valor

    3. Set -> Estructura que guarda varios valores pero NO permite repetidos
           -> No tiene indices
           -> No ordenado

    4. Tuple -> Colección ordenada e INMUTABLE -> Array
"""