"""
# Titulo: Desafío 5 Herencia
# Autor: Anthony Martinelli
# Fecha: 14/10/2024
# Descripción:
# Implementa una jerarquía de clases para representar diferentes tipos de empleados en una biblioteca,
# utilizando herencia múltiple y composición.
"""

# Definimos la clase base Empleado
class Empleado:
    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def trabajar(self):
        print(f"\n{self.nombre} está trabajando como {self.cargo}")


# Definimos la clase base Administrador
class Administrador:
    def __init__(self, area_administrativa):
        self.area_administrativa = area_administrativa

    def administrar(self):
        print(f"Está administrando el área de {self.area_administrativa}")


# Definimos la clase base Mantenimiento
class Mantenimiento:
    def __init__(self, area_mantenimiento):
        self.area_mantenimiento = area_mantenimiento

    def mantener(self):
        print(f"Está realizando mantenimiento en el área de {self.area_mantenimiento}")


# Creamos una clase Gerente que hereda de Empleado y compone con Administrador
class Gerente(Empleado):
    def __init__(self, nombre, edad, cargo, area_administrativa):
        super().__init__(nombre, edad, cargo)
        self.administrador = Administrador(area_administrativa)

    def administrar(self):
        self.administrador.administrar()


# Creamos una clase Tecnico que hereda de Empleado y compone con Mantenimiento
class Tecnico(Empleado):
    def __init__(self, nombre, edad, cargo, area_mantenimiento):
        super().__init__(nombre, edad, cargo)
        self.mantenimiento = Mantenimiento(area_mantenimiento)

    def mantener(self):
        self.mantenimiento.mantener()


# Creamos una clase Voluntario que hereda de Empleado
class Voluntario(Empleado):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad, cargo)

    def ayudar(self):
        print(f"{self.nombre} tiene {self.edad} años, tratenlo bien!")


# Instanciamos objetos de las clases Gerente, Tecnico y Voluntario
gerente = Gerente("Juan Carlos", 35, "Gerente", "Recursos Humanos")
tecnico = Tecnico("María Rodriguez", 28, "Técnico", "Sistemas Informáticos")
voluntario = Voluntario("Pedro García", 22, "Voluntario")

# Llamamos a los métodos de cada objeto
gerente.trabajar()
gerente.administrar()

tecnico.trabajar()
tecnico.mantener()

voluntario.trabajar()
voluntario.ayudar()