#ejercicio
#crea una clase llamada Alumno 
#el alumno tiene nombre, curso y fecha de matricula
#alta a los siguientes alumnos
#juan lópez, DAM1, 10-01-2023
#maria pérez, DAW1,15-01-2023
#crea metodo para mostrar detalle de alumno
#crea un metodo que muestre la fecha de hoy: genérico -- estático

from datetime import date 

class Alumno:
    def __init__(self,nombre,curso,fecha_matriculacion) -> None:
        self.nombre=nombre
        self.curso=curso
        self.fecha_matriculacion=fecha_matriculacion
    def detalle(self):
        print(f'El alumno se llama {self.nombre}, matrícula en {self.curso} a partir de {self.fecha_matriculacion}')
    @staticmethod
    def consultarfecha():
        print(f'la fecha de hoy es {date.today}')

a1=Alumno('Juan lópez', 'DAM1', '10-1-2023')
a2=Alumno('Maria Pérez', 'DAW1', '15-1-2023')
a1.detalle()
a2.detalle()
a1.consultarfecha()
a2.consultarfecha()