# ---- Convención de nomenclatura ----
print("\n--- Convención de nomenclatura ----")
variable = "Variable en minúscula"
my_variable = "Variable en snake case"
my_int_variable = 5

print(variable)
print(my_variable)
print(my_int_variable)

name = "Martín"
age = 18
print("Hi, my name is", name , "and I'm", age) # Concatenación de variables en un print

print(type(age))
age = str(age) # Cambio de tipo de dato
print(type(age))

# ---- Algunas Funciones del sistema ----
print("\n---- Funciones del sistema ----")

# Length
print(len(name)) 
longitud = len(name)
print("Martín tiene", longitud , "letras")

# Input
name = input("Ingresa tu nombre:")
print(name)

# Funciones de Manipulación de Datos (simple)
vector = [0, 11, 24, 3, 14]
print(vector)
print(sorted(vector))
vector.append("a")
print(vector)
vector.insert(0, "z")
print(vector)
vector.pop()
print(vector)