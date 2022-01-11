# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:50:39 2022

@author: Yam
"""

import pandas as pd
import numpy as np

data= pd.read_csv('C:/Users/Yam/Desktop/OCC/Housing.csv')
print(data.describe(include='all'))
columns_dt=list(data.columns) # Columnas que conforman el DF
missing_values_count = data.isnull().sum() # Conteo de datos faltantes por columna

