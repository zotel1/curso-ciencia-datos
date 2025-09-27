import pandas as pd
import numpy as np


print("Primer dato con numpy")
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.ndim) 

print("Segundo dato con numpy")
b = np.array([[1, 2, 3], 
              [4, 5, 6]])
print(b)
print(b.ndim)
print(b.shape) # Nos dice cuantas filas y cuantas columnas tiene
print(b.dtype) # Nos dice el tipo de dato que tiene el array

print("Tercer dato con numpy")
c = np.array([1, 2.2, 3])
print(c)
print(c.dtype)

print("Cuarto dato con numpy")
d = np.zeros((2, 3))
print(d)
d= np.ones((2, 3))
print(d)
d = np.random.rand(2, 3)
print(d)
d = np.arange(10, 100, 5)
print(d)
d = np.linspace(0, 2, 25)
print(d)

print("Operaciones con arreglos")
"""
no se puede hacer, hay que meter un for recorrer las listas y empezar a realizar la operacion
a_por_c = a * c
print(a_por_c)

a_menos_c = a - c
print(a_menos_c)"""
print(b)
mayores = b > 3
print(mayores)

mostrar_mayores_que_3 = b[b > 3]
print(mostrar_mayores_que_3)
es_par = b % 2 == 0
print(es_par)

print("Indices")

print(b[1,0])
print(b[[1,0], [1,0]]) # Nos trae los elementos 1,1 y 0,0
       #primero x y despues y
print("Operadores booleanos")
print(b[b==5])
print(b[(b>2) & (b<5)]) # and
print(b[(b<2) | (b>5)]) # or
print(b[~(b>5)]) # not
print(b[b!=5])

print(f" valor de a: {a}")
print(a[1:])
print(a[:])
print(a[:2])

print(f"Valor de b: {b}")
print(b[:2]) # Nos trae las dos primeras filas
print(b[:, :2]) # Nos trae todas las filas y las dos primeras columnas
print(b[1, :2]) # Nos trae la fila 1 y las dos primeras columnas
print(b[1, 1:]) # Nos trae la fila 1 y desde la columna 1 hasta el final