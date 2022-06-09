from distutils.log import info
import pandas as pd

rutaFileCsv ='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str):
    datos = pd.read_csv (rutaFileCsv)
    informacion = datos[["Country","Language","Gross Earnings"]]
    resumen = informacion.pivot_table(index=["Country","Language"]).head(10)

    return resumen

print(listaPeliculas(rutaFileCsv))
