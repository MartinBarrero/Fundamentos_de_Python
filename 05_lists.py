### Lists ###

# Definición
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [5, 10, 15, 20, 25]
print(my_list)
print(len(my_list))

my_other_list = [18, "Martín", "Barrero"]

# --- Acceso a elementos y búsqueda ---
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
# print(my_other_list[3]) IndexError out of range
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
# print(my_other_list[-4]) IndexError out of range

print(my_other_list.count("Martín")) # Con tilde -> 1
print(my_other_list.count("Martin")) # Sin tilde -> 0

my_list.append(5)
print(my_list)
print(my_list.count(5))

# --- Desempaquetar elementos --- 
age, name, lastname = my_other_list
print(age)
print(lastname)

# name = my_other_list[4] IndexError out of range

# Concatenación
print(my_list + my_other_list)

# --- Creación, inserción, actualización y eliminación ---
my_other_list.append("Python")
print(my_other_list)

my_other_list.insert(1, "White")
print(my_other_list)

my_other_list[1] = "Blue"
print(my_other_list)

my_other_list.remove(18) # Elimina con valor 
print(my_other_list)

# my_other_list.remove(20) ValueError -> No había este valor en la lista

print(my_other_list.pop()) # Muestra el elemento eliminado
print(my_other_list) # Muestra la lista sin el elemento eliminado

my_pop_element = my_other_list.pop(0)
print(my_pop_element)
print(my_other_list)

del my_other_list[1] # Elimina con indice 
print(my_other_list)

# --- Operaciones con listas ---
my_new_list = my_list.copy()
my_list.clear()
print(my_new_list)
print(my_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# --- Sublistas ---
print(my_new_list[1:3])
