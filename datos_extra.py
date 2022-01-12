# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:01:53 2022

@author: Yam
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

data= pd.read_csv('C:/Users/Yam/Desktop/OCC/Housing.csv')
print(data.describe(include='all'))
columns_dt=list(data.columns) # Columnas que conforman el DF
missing_values_count = data.isnull().sum() # Conteo de datos faltantes por columna

num_data=(input("Cantidad de registros a agregar :"))
num_data=int(num_data)
# Distribucion de datos
col_v=columns_dt[1:]
sns.displot(data,kde=True)
for i in range(len(col_v)):
    colum=col_v[i]
    sns.displot(data[colum],kde=True)
    plt.title('Distribucion')

# Datos numericos
data_numeric = data.select_dtypes(include=[np.number])
numeric_cols = data_numeric.columns.values

# Datos cualitativos
datos_non_numeric = data.select_dtypes(exclude=[np.number])
non_numeric_cols = datos_non_numeric.columns.values

#Obtener los datos unicos por atributo 
uniq_data_clums=[]
for i in range(len(col_v)):
    variables = data[col_v[i]].unique() 
    uniq_data_clums.append(variables)
uniq_data_clums

#Generar datos sinteticos a partir de metodo ruleta
bd=[]
for j in range(num_data):
    row=[]
    for i in range(len(col_v)):
        item_counts_key = data[col_v[i]].value_counts().index.tolist() #Valor unico
        item_counts = data[col_v[i]].value_counts(normalize=True) #Probabilidad de que este valor aparezca en la base de datos
        cumsumP=item_counts.cumsum() #Suma acumulativa de la probabilidad para priorizar valores
        w=cumsumP.to_numpy() 
        r=random.random() #Generar un porcentaje aleatorio
        magico=np.argwhere(r <= w) #Buscar el porcentaje mas cercano alcanzado por los valores unicos
        x=int(magico[0]) #Index de dicho valor
        dato=item_counts_key[x] #Obtener el valor para generar dato sintetico
        row.append(dato) 
    bd.append(row) #fila sintetica


#Crear un Marco de datos de los datos sinteticos
d_syn=pd.DataFrame(bd, columns=col_v)

data2=data.copy()
data2=data2.drop(data.columns[[0]], axis='columns')

#Agregar datos sinteticos a la copia de los datos originales
d_final=pd.concat([data2, d_syn], ignore_index=True)
d_final.insert(0, " ", np.arange(1,len(d_final)+1), True) 

#Revisar que la distribucion de datos sea semejante a la inicial
sns.displot(d_final,kde=True)
for i in range(len(col_v)):
    colum=col_v[i]
    sns.displot(d_final[colum],kde=True)
    plt.title('Distribucion')
    
# Guardar como csv el Dataset resultante
d_final.to_csv('data_Housing_out.csv', index=False)
