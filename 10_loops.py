### Loops ###

# --- While ---
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es mayor o igual a 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# --- For ---

my_list = [18, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Martín", "Barrero", "Python")

for element in my_tuple:
    print(element)

my_set = {"Martín", "Barrero", 18}

for element in my_set:
    print(element)

print("\n")

my_dict = {"Name": "Martín",
           "Lastname": "Barrero",
           "Age": 18,
           1: "Python"}

for element in my_dict:
    print(element)
    if element == "Age":
        break

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Age":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")