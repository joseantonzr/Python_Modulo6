# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:39:57 2024

@author: josea
"""

# Libreria para excel
import pandas as pd 

# Uso de libreria para el try y exception
import sys

# MySQL conexion a la base
from sqlalchemy import create_engine

try:
    # Leer plantilla a la base
    print('Leyendo archivo...')
    ds = pd.read_excel(r'C:\Users\josea\OneDrive\Escritorio\Modulo FInal\Modulo_6\Reportes\CarPrice_Assignment_DS1_Output.xlsx')

    # Cambia el nombre de las columnas de la plantillas al nombre de los campos de la tabla
    ds = ds.rename(columns={
        'car_ID':'car_ID',
        'symboling':'symboling',
        'CarName':'CarName',
        'fueltype':'fueltype',
        'aspiration':'aspiration',
        'doornumber':'doornumber',
        'carbody':'carbody',
        'drivewheel':'drivewheel',
        'enginelocation':'enginelocation',
        'wheelbase':'wheelbase',
        'carlength':'carlength',
        'carwidth':'carwidth',
        'carheight':'carheight',
        'curbweight':'curbweight',
        'enginetype':'enginetype',
        'cylindernumber':'cylindernumber',
        'enginesize':'enginesize',
        'fuelsystem':'fuelsystem',
        'boreratio':'boreratio',
        'stroke':'stroke',
        'compressionratio':'compressionratio',
        'horsepower':'horsepower',
        'peakrpm':'peakrpm',
        'citympg':'citympg',
        'highwaympg':'highwaympg',
        'price':'price',
        'Price Predictions':'PricePredictions'
    })

except Exception as e:
    print('Error: No se pudo leer el archivo: {0}'.format(str(e)))
    sys.exit(1)

try:
    # Crear conexion a cars_sv
    sys = create_engine('mysql+mysqlconnector://root:cloe2223@localhost:3306/cars_sv')

    # Insert a tabla de auto_tech
    print('Insertando a cars_sv...\n')
    ds.to_sql('pricepredictions', con=sys, if_exists='append', chunksize=1000, index=False)
    print('--- Ejecucion finalizado ---')

except Exception as e:
    print('Error: Problema con la conexion a sys: {0}'.format(str(e)))
    sys.exit(1)