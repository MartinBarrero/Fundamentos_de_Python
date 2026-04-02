### Classes ###

# --- Definición ---

class MyEmptyPerson:
    pass # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())
print("\n")

# --- Clase con constructor, funciones y propiedades privadas y públicas

class Person:
    def __init__(self, name, lastname):
        self.full_name = f"{name} {lastname}" # Propiedad pública
        self._name = name # Propiedad privada

    def get_name(self):
        return self._name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Martín", "Barrero")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_person.full_name = "Juan Miguel Herrera"
print(my_person.full_name)
print(my_person.get_name()) # No se puede acceder para modificarlo porque es _name es privado
my_person.walk()