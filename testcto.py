"""Librerias"""

from sqlalchemy import create_engine
import mysql.connector
import pymysql
import pandas as pd

""" Fin Librerias"""

"""variables"""
sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3306)
dbConnection = sqlEngine.connect()

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

""" Fin variables"""

"""Programa"""
print(mensaje)
print(desarrollador)
"""conexión y configuración de bd en mysql"""
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='testcto')
print("conectado a: ", cnx)
cnx.close()
"""dataframe mysql"""
dataframe = pd.read_sql("select * from testcto.cities", dbConnection);
pd.set_option('display.expand_frame_repr', False)

"""Funciones de menú"""


def getPais():
    """Busqueda en frame de pais"""
    pais = str(input("Introduce nombre de pais: "))
    countryFilter = dataframe[dataframe['country'] == pais]
    print(" Estado - Ciudad - población")

    for i in countryFilter.index:
        print(countryFilter.loc[i, 'state'], " - ", countryFilter.loc[i, 'name'], " - ",
              countryFilter.loc[i, 'population'])


def getEstado():
    """Busqueda en frame de pais"""
    estado = str(input("Introduce nombre de estado: "))
    estadoFilter = dataframe[dataframe['state'] == estado]

    print(" Ciudad - población")

    for i in estadoFilter.index:
        print(estadoFilter.loc[i, 'name'], " - ",
              estadoFilter.loc[i, 'population'])


def getCiudad():
    """Busqueda en frame de pais"""
    ciudad = str(input("Introduce nombre de ciudad: "))
    ciudadFilter = dataframe[dataframe['name'] == ciudad]

    print(" Ciudad - población - Pais - Estado")

    for i in ciudadFilter.index:
        print(ciudadFilter.loc[i, 'name'], " - ",
              ciudadFilter.loc[i, 'population'], " - ", ciudadFilter.loc[i, 'country'], " - ",
              ciudadFilter.loc[i, 'state'])


"""menú de opciones """


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce opción: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print("1. Buscar por pais")
    print("2. Buscar por estado")
    print("3. Buscar por ciudad")
    print("4. Salir")

    print("Elige una opción")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        getPais()
    elif opcion == 2:
        getEstado()
    elif opcion == 3:
        getCiudad()
    elif opcion == 4:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")

dbConnection.close()
