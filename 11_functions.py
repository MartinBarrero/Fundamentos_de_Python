### Functions ###

# --- Definición ---

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# --- Función con parámetros de entrada/argumentos ---

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(20, 30)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# --- Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

# --- Función con parámetros de entrada/argumentos por clave

def print_name(name, lastname):
    print(f"{name} {lastname}")

print_name("Martín", "Barrero")

# --- Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, lastname, alias = "Sin alias"):
    print(f"{name} {lastname} {alias}")

print_name_with_default("Martín", "Barrero") # Como ya se ha asignado el valor por defecto no genera problema al no incluir ese parámetro
print_name_with_default("Martín", "Barrero", "Tin")

# --- Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts): # Número de parámetros dinámicos
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("hola", "adios", "Python") # No se envía una lista sino como parámetros independientes
