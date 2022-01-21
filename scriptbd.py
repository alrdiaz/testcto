"""Librerias"""

from datetime import date
import pandas as pd
from progress.bar import Bar

import mysql.connector

"""declaraciòn de funciones y variables"""

mensaje = """
─────────────────────────────────────────────────────────────────
─██████████████─████████████████───██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░████████░░██───██░░██████████─██░░██████░░██─
─██░░██─────────██░░██────██░░██───██░░██─────────██░░██──██░░██─
─██░░██████████─██░░████████░░██───██░░██─────────██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██─────────██░░██──██░░██─
─██░░██████████─██░░██████░░████───██░░██─────────██░░██──██░░██─
─██░░██─────────██░░██──██░░██─────██░░██─────────██░░██──██░░██─
─██░░██████████─██░░██──██░░██████─██░░██████████─██░░██████░░██─
─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████████─██████████████─██████████████─                                                                                                                                                              
 """
desarrollador = """                                        By Alejandro Romero
-----------------------------------------------------------------
"""

listanuevawbs = []
listanuevoproyecto = []
listaevaluados = []
hoy = str(date.today())
CITIESFILE = "cities.xlsx"
STATEFILE = "states.xlsx"
COUNTRYFILE = "countries.xlsx"
sql = "INSERT INTO cities (id_city, name, state, country, population) VALUES (%s, %s, %s, %s, %s)"

"""Estrucutra de script"""

print(mensaje)
print(desarrollador)

folder = input("Ingrese ruta local de archivos cities.xlsx, states.xlsx y countries.xlsx: ")

citiesFile = folder + "/" + CITIESFILE
statesFile = folder + "/" + STATEFILE
countriesFile = folder + "/" + COUNTRYFILE

citiesFrame = pd.read_excel(citiesFile, sheet_name='result 1')
statesFrame = pd.read_excel(statesFile, sheet_name='result 1')
countriesFrame = pd.read_excel(countriesFile, sheet_name='result 1')
"""conexión y configuración de bd en mysql"""
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='testcto')

mycursor = cnx.cursor()
mycursor.execute(
    "CREATE TABLE cities (id INT AUTO_INCREMENT PRIMARY KEY, id_city INT ,name VARCHAR(255),state VARCHAR(255),country VARCHAR(255), population INT)")

id = citiesFrame['ID_CITY']
maximo1 = len(id)

print("conectado a: ", cnx)
print(maximo1, " ciudades wait....")
bar = Bar(' Procesando ciudades: ', max=maximo1)
for i in citiesFrame.index:
    bar.next()
    """Atributos de clase ciudades"""
    city_id = int(citiesFrame.loc[i, 'ID_CITY'])
    city_name = str(citiesFrame.loc[i, 'NAME']).rstrip()
    city_population = int(citiesFrame.loc[i, 'POPULATION'])
    state_id = int(citiesFrame.loc[i, 'ID_STATE'])
    """Busqueda en frame de estados"""
    stateFilter = statesFrame.set_index('ID_STATE')
    state_name = str(stateFilter.loc[state_id, 'NAME'])
    state_countryid = int(stateFilter.loc[state_id, 'ID_COUNTRY'])
    """Busqueda en frame de paises"""
    countryFilter = countriesFrame.set_index('ID_COUNTRY')
    country_name = str(countryFilter.loc[state_countryid, 'NAME'])
    val = (city_id, city_name, state_name, country_name, city_population)
    mycursor.execute(sql, val)
    cnx.commit()
    print("city inserted: ", city_name)

bar.finish()

cnx.close()
print("Finalizado")
