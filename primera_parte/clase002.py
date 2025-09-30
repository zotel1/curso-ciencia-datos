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

"""
Dataframes
La estructura estrella de pandas, es una tabla 2-D en donde:
- Cada fila es una observacion(registro)
- Cada columna es una variable(campo)
y todo lleva etiquetas(nombre de filas y columnas)
"""

datos = {
    'Nombre': [
        'Adrian', 'Bea', 'Carlos', 'Diana', 'Eva', 
        'Fernando', 'Gabriela', 'Hector', 'Ines', 'Javier'
        ],
    'Producto': [
        'Pantalon', 'Camisa', 'Zapatos', 'Falda',
        'Corbata', 'Cinturon', 'Sombrero', 'Bufanda', 'Guantes', 
        'auriculares'
        ],
    'Categoria': ['Ropa', 'Ropa', 'Calzado', 'Ropa', 'Ropa', 
                  'Accesorios', 'Accesorios', 'Accesorios', 'Accesorios', 'Accesorios'],
    'Precio': [20, 15, 30, 25, 18, 12, 10, 22, 8, 14],
    'Cantidad': [2, 3, 1, 4, 2, 5, 3, 2, 6, 4],
    'Fecha': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
              '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24'
              ],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza',
                'Malaga', 'Murcia', 'Palma', 'Bilbao', 'Alicante'
                ],
     'Satisfaccion': [4, 5, 3, 4, 5, 2, 4, 3, 5, 4] 
}

df = pd.DataFrame(datos)
print(df)
print(df.dtypes)    
print("Mostramos la informacion del DataFrame")
info = df.info()
print(info)

print("Mostramos la descripcion estadistica del DataFrame")
descr = df.describe()
print(descr)
