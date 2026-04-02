### Sets ###

# --- Definición ---

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Incialmente es un diccionario

my_other_set = {"Martín", "Barrero", 18} # Ahora si es un set
print(type(my_other_set))

print(len(my_other_set))

# --- Inserción ---
my_other_set.add("Python")
my_other_set.add("a")
print(my_other_set) # {'Barrero', 'a', 'Python', 18, 'Martín'} -> Un set no es una estructura ordenada

my_other_set.add("Python") # Un set no admite repetidos
print(my_other_set)

# --- Busqueda ---
print("Martín" in my_other_set)
print("martin" in my_other_set)

# --- Eliminación ---
my_other_set.remove("Martín")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# --- Trasnformación ---
my_set = {"Martín", "Barrero", 18}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# --- Otras operaciones ---
my_other_set = {"Java" , "C" , "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))