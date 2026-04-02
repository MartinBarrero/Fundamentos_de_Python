name = "Martín"
lastname = "Barrero"
age = 18

print(len(name))
print(len(lastname))

print(name + " " + lastname)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String\n\tcon tabulación"
print(my_tab_string)

# Formateo
print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age))
print("Mi nombre es " + name + " " + lastname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f= language
print(a)
print(b)
print(f)

# División
language_slice = language[1:5]
print(language_slice)

language_slice = language[0:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funtions
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo