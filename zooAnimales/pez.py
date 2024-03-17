from animal import Animal

class Pez(Animal):
    
    salmones = 0
    bacalaos = 0
    listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, cantidadAletas = 0 ) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls.listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls.listado
    
    def cantidadPez(self):
        
        return len(Pez.listado)
    
    def setColorPiel(self, colorEscamas):
        
        self._colrEscamas = colorEscamas
        
    def getColorEscamas(self):
        
        return self._colorEscamas
    
    def setcantidadAletas(self, cantidadAletas):
        
        self._cantidadAletas = cantidadAletas
        
    def getcantidadAletas(self):
        
        return self._cantidadAletas
    
    def movimiento(self):
        
        return "nadar"
    
    @classmethod
    def crearSalmon(nombre, edad, genero):
        
        nuevoSalmon = Pez(nombre, edad, "selva", genero, "rojo", True )
        Pez.salmones+=1
        return nuevoSalmon
        
    @classmethod
    def crearBacalao(nombre, edad, genero):
        
        nuevoBacalao = Pez(nombre, edad, "selva", genero, "negro y amarillo", False)
        Pez.bacalaos+=1
        return nuevoBacalao
    