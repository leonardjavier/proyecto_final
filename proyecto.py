#librerias 

## sistema 
import sys
import os
from glob import glob

## extracion de datos
import urllib.request, urllib.error, urllib.parse, operator

## manipulacion de datos 
import pandas as pd


PATH = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/RestaurantRating/Restaurant%20customer%20data.csv"


try:
    # Solicitud de datos en la web
    url_data = urllib.request.urlopen(PATH)

    # Creacion del data frame
    df_origin = pd.read_csv(url_data, index_col="userID")

    # Filtrado de las columnas del data frame
    df_filtro_columnas = df_origin[["smoker","dress_preference","drink_level","birth_year","activity","color","budget","height","latitude","longitude"]]
    # print(df_fitro_columnas)

    # Filtrado de valores 
    df_filtros_fila= df_filtro_columnas[df_filtro_columnas["dress_preference"] != "?"]
    print(df_filtros_fila.info())



    





except Exception as e:
    print(e)

