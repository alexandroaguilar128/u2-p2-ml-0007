import numpy as np
# Alexandro Aguilar NC 0007
# Ejemplo de numpy  Numerical Python
print("--- Espaciado Linealmente en array --- 0007")
arre = np.linspace(start=0, stop=5, num = 5)
print(arre)
print("--- Matriz identidad en 2D array --- 0007")
matriz = np.eye(3)
print(matriz)
print("--- Genera numeros al azar (Aleatorios) en 2D array --- 0007")
numale = np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("generar 9 numeros aleatorios entre 0 y 1")
numale = np.random.random((3,3)) # genera 9 numeros aleatorios
print(numale)
# como generar 9 números aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3x3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=(3, 3))
print(arre)
print("Alexandro Aguilar NC 0007")
