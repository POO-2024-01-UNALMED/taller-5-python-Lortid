from animal import Animal

class Mamifero(Animal):
    
    caballos = 0
    leones = 0
    listado = []
    
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, pelaje = False, patas = 0 ) :
        
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    @classmethod
    def setListado(cls, listado):
        
        cls.listado = listado 
    
    @classmethod
    def getListado(cls):
        
        return cls.listado
    
    def cantidadCaballos(self):
        
        return len(Mamifero.listado)
    
    def setPelaje(self, Pelaje):
        
        self._pelaje = Pelaje
        
    def getPelaje(self):
        
        return self._pelaje
        
    def setPatas(self, patas):
        
        self._patas = patas
        
    def getPatas(self):
        
        return self._patas
    
    @classmethod
    def crearCaballo(nombre, edad, genero):
        
        nuevoCaballo = Mamifero(nombre, edad, "pradera", genero, True, 4 )
        Mamifero.caballos+=1
        return nuevoCaballo
        
    @classmethod
    def crearLeon(nombre, edad, genero):
        
        nuevoLeon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones+=1
        return nuevoLeon
    