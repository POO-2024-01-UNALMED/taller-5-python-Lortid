from mamifero import Mamifero
from anfibio import Anfibio
from ave import Ave
from pez import Pez
from reptil import Reptil

class Animal:
    
    _totalAnimales = 0

def __init__ (self, nombre = None, edad = 0, habitat = None, genero = None):
    
    self._nombre = nombre
    self._edad = edad
    self._habitat = habitat
    self._genero = genero
    Animal._totalAnimales +=1

@classmethod
def setTotalAnimales(cls, totalAnimales):
    
    cls._totalAnimales = totalAnimales

@classmethod
def getTotalAnimales(cls):
    
    return cls._totalAnimales
    
def setNombre(self, nombre):
    
    self._nombre = nombre
    
def getNombre (self):
    
    return self._nombre

def setEdad(self, edad):
    
    self._edad = edad

def getEdad(self):
    
    return self._edad

def setHabitat(self, habitat):
    
    self._habitat = habitat
    
def getHabitat(self):
    
    return self._habitat

def setGenero(self, genero):
    
    self._genero = genero

def getGenero(self):
    
    return self._genero

def setZona(self, zona):
    
    self._zona = zona

def getZona(self):
    
    return self._zona
@classmethod
def totalPorTipo(cls):
    
    return f"Mamiferos: {Mamifero.cantidadMamiferos()} \nAves: {Ave.cantidadAves()} \nReptiles: {Reptil.cantidadReptiles()} \nPeces: {Pez.cantidadPeces()} \nAnfibios: {Anfibio.cantidadAnfibios()} "


def __str__(self):
    
    if self._zona == None:
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    
    else:
        
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self.getZona().getNombre()}, en el {self._zona.getZoo().getNombre}"

def movimiento(self):
    
    return "desplazarse"