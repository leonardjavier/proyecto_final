import urllib.request, urllib.error, urllib.parse, operator
import pandas


PATH = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/RestaurantRating/Restaurant%20customer%20data.csv"


try:
    url_data = urllib.request.urlopen(PATH)
    for linea in url_data:
        print(linea.decode())  
except Exception as e:
    print(e)






