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
    url_data = urllib.request.urlopen(PATH)
    df = pd.read_csv(url_data, index_col="userID")
    print(df)

except Exception as e:
    print(e)

