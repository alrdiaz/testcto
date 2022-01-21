# testcto
Se debe desarrollar un algoritmo que permita a cualquier usuario consultar la población por ciudades según el nivel que se consulte, es decir, si se busca un país, se debería mostrar todos sus estados y cada estado sus ciudades con su respectiva población; sí se consulta un estado debe traer el estado con todas sus ciudades y su respectiva población; y por último sí se consulta una ciudad se debe mostrar su población.

## Base de datos 
**Crear base de datos local con motor de base de datos mySQL con los siguientes atributos:**
- nombre: testcto
- user='root'
- passwoord:
- host='localhost'
- port: 3306


## scriptbd
1. Instalar:
- [datetime](https://pypi.org/project/DateTime/) => pip install DateTime
- [pandas](https://pypi.org/project/pandas/)=> pip install pandas
- [progress.bar](https://pypi.org/project/progress_bar/)=> pip install progress_bar
- [mysql.connector](https://pypi.org/project/mysql-connector/) => pip install mysql-connector
- Script para lectura de archivos .xlsx con la libreria pandas de python.
- suministrar la ruta local de los archivos suministrados.
- **se leeran los archivos y basados en sus relaciones de llaves foraneas se creara una tabla con los campos:**
- id autoincremental
- id_city: cçodigo de ciudad
- name: nombre de ciudad
- state: nombre de estado
- country: nombre de pais
- population: numero de la población

## script=>testcto
script con las opciones de busqueda en la base de datos a travez de la consulta inicial a la base de datos y posteriormente un load a un dataframe para realizar los filtros para las busquedas.


