import csv
import io
import urllib.request
import pandas as pd
import requests as requests

import csv
import requests

#Descarga del dataset desde repo
req = requests.get("https://raw.githubusercontent.com/FauDavid/MFSDOBNN-IC-TP/main/dataset.csv")
url_content = req.content
csv_file = open('downloaded.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

#Cargar dataset local
data = pd.read_csv("downloaded.csv")
print(data.head())

