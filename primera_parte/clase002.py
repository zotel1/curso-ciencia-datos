"""
Pandas
"""
import pandas as pd
import numpy as np

nombres = ['Luis', 'Ana', 'Carlos']
print(nombres)
panda_series = pd.Series(nombres)
print(panda_series)
print(pd.Series([1,2, None, 4]))

nombres_cal = {
    'Adrian': 8,
    'Bea': 7,
    'Carlos': 6
}
print(f"Diccionario: {nombres_cal}")
s = pd.Series(nombres_cal)
print(s)
print(s.index)
print(s.values)
print(f" el indice es {s.index[1]} y el valor es {s['Bea']}")

print("Datos mas complejos")
nombres_ejemplo_dos = [('Adrian', 'Sanchez'), ('Bea', 'Lopez'), ('Carlos', 'Gomez')]
z = pd.Series(nombres_ejemplo_dos)
print(z)

i = pd.Series(['Matematicas', 'Fisica', 'Quimica'], index=['Adrian', 'Bea', 'Carlos'])
print(i)
"""
loc e iloc son dos modos de indexar y cortar datos en un DataFrame o Series de pandas.
loc funciona en base a etiquetas, mientras que iloc funciona en base a posiciones enteras.
"""
print(s.loc['Bea'])
print(s.iloc[2])

#Operaciones sobre Series

cal = pd.Series([90, 72, 85, 60])
print(cal)
total = np.sum(cal)
print(f"El total es {total/len(cal)}")

numbers = pd.Series(np.random.randint(1, 1000, 10000))
numbers.head() # head muestra los primeros 5 elementos
print(numbers)
print(numbers.describe()) # describe muestra estadisticas basicas

print("Medicion de tiempo")
#%%timeit -n 100 
total = 0
for i in numbers:
    total += i
total/len(numbers)
print(total/len(numbers))

print(s)
nuevos_nombres = pd.Series({
    'Karla': 9,
    'Luis': 8,
    'Marta': 7
})
s = pd.concat([s, nuevos_nombres])
print(s)


