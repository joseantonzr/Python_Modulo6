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
    ds = pd.read_excel(r'C:\Users\josea\OneDrive\Escritorio\Depuracion_Auto_Tech.xlsx')

    # Cambia el nombre de las columnas de la plantillas al nombre de los campos de la tabla
    ds = ds.rename(columns={
        'Make':'Make',
        'Model':'Model',
        'Price USD':'PriceUSD',
        'Year_a':'Year_a',
        'sale ':'SaleStatus',
        'Kilometer':'Kilometer',
        'Fuel Type':'FuelType',
        'Transmission':'Transmission',
        'Color':'Color',
        'Owner_a':'Owner_a',
        'Seller Type':'SellerType',
        'Engine_a':'Engine_a',
        'Max Power':'MaxPower',
        'Max Torque':'MaxTorque',
        'Drivetrain':'Drivetrain',
        'Length_a':'Length_a',
        'Width':'Width',
        'Height':'Height',
        'Seating Capacity':'SeatingCapacity',
        'Fuel Tank Capacity':'FuelTankCapacity'
    })

except Exception as e:
    print('Error: No se pudo leer el archivo: {0}'.format(str(e)))
    sys.exit(1)

try:
    # Crear conexion a cars_sv
    sys = create_engine('mysql+mysqlconnector://root:cloe2223@localhost:3306/cars_sv')

    # Insert a tabla de auto_tech
    print('Insertando a cars_sv...\n')
    ds.to_sql('auto_tech', con=sys, if_exists='append', chunksize=1000, index=False)
    print('--- Ejecucion finalizado ---')

except Exception as e:
    print('Error: Problema con la conexion a sys: {0}'.format(str(e)))
    sys.exit(1)