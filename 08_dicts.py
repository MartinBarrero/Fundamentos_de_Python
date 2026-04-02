### Dictionaries ###

# --- Definition ---
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Martín",
                 "Lastname": "Barrero",
                 "Age": 18,
                 1: "Python"}

my_dict = {
    "Name": "Martín",
    "Lastname": "Barrero",
    "Age": 18,
    "languages": {"Python", "C", "C++"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

# --- Búsqueda ---
print(my_dict[1])
print(my_dict["Name"]) # Busca por clave y da el valor

print("Martín" in my_dict) # Verifica si existe en el dictionary como clave
print("Lastname" in my_dict)
print("Age" in my_dict)
print(18 in my_dict)

# --- Inserción ---
my_dict["Calle"] = "Calle 12"
print(my_dict)

# --- Actualización ---
my_dict["Name"] = "Pedro"
print(my_dict["Name"])

# --- Eliminación ---
del my_dict["Calle"]
print(my_dict)

# --- Otras operaciones ---
print("\n")
print(my_dict.items()) # Separa la clave valor en una dupla
print(my_dict.keys())
print(my_dict.values())

my_list = ["Name", 1, "Floor"]

my_new_dict = dict.fromkeys((my_list)) # Creación de diccionario sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, 1)
print((my_new_dict))

# --- Jugando con los tipos de datos ---
print("\n")
my_values = my_new_dict.values()
print(type(my_values))
print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))