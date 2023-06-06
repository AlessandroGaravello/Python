#POO

class Prueba: #definir una clase
    nombre='juan' #atributo de clase


    def __init__(self) -> None: #constructor
        pass
    def saludar(self): #metodo de instancia. palabra self indica la instancia
        print(self.nombre) #acceso a atributo del objeto
    @classmethod #decorador
    def metodoClase(cls):
        print(f'esto es un método de clase {cls}')
        print(cls.nombre) #gestiona  atributos y metodos de la clase
    @staticmethod
    def metodoEstatico():
        print('esto es un método estatico') # no puede gestionar ni la instancia ni la clase


#utilizar clase: instanciar un objeto
prueba1=Prueba()#llama al constructor
prueba1.nombre='marta'
prueba1.saludar()
prueba1.metodoClase()
prueba1.metodoEstatico()


#herencia. herencia multiple. sobreescritura. constructor super

class Padre: #clase base, padre, Superclase
    color='red'
    def __init__(self,categoria) -> None:
        self.categoria=categoria
    @staticmethod
    def consultar():
        print('resultado de clase Padre')

class General:
    color='blue'

#Python soporta herencia multiple en orden de las comas
class Hija(Padre,General): #clase derivada, hija, Subclase
    unidades=20
    def __init__(self,precio,categoria) -> None:
        super().__init__(categoria)#Sin puntos
        self.precio=precio
    @staticmethod
    def consultar():#sobreescritura
        print('Consultando ddesde la hija')

h1=Hija(19.95, 'oficial') #instanciar clase
print(f'el total es {h1.unidades*h1.precio}')
print(f'el color elegido es {h1.color}')#usar atributos de clase base
h1.consultar()#usar metodos de clase base

#POO Python. Implementar interfaces.

class BuenosHabitos:#es una interface
    def comer():#sin implementar
        pass#el método esta sin implementar
    def dormir():
        pass
    def estudiar():
        pass

#al implementar una interfaz, en Python NO error si te falta algún método
class Deportista(BuenosHabitos):#implementas la interface BuenosHabitos
    @staticmethod
    def comer():
        print('comes pasta')
    @staticmethod
    def dormir():
        print('duermes 8 horas y siesta')
    @staticmethod
    def estudiar():
        print('no estudias')
class Estudiante(BuenosHabitos):
    @staticmethod
    def comer():
        print('comes pescado')
    @staticmethod
    def dormir():
        print('duermes 7 horas y sin siesta')
    @staticmethod
    def estudiar():
        print('no estudias')
    
d1=Deportista()
d1.comer()

#POO python. encapsulamiento***

class Cliente:
    __descuento=True #atributo private con __
    def __init__(self,nombre) -> None:#constructor
        self.nombre=nombre
    def __saludar(self):#método private con __
        print(f'hola {self.nombre}')
    def despedir(self):
        print(f'adiós {self.nombre}')

c1=Cliente('juan lópez') #instanciar
c1.__saludar()