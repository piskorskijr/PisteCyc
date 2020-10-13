import time
import requests
import json
import datetime
import signal
import sys
import schedule
import math
from math import*
import datetime
import MySQLdb
import random
from time import sleep

#Connexion a la base de donnees SQL 
db = MySQLdb.connect(host="localhost", user="root", passwd="pass", db="TestProjetYES")
curs= db.cursor()
#Heure actuelle
tday = datetime.date.today()
url = 'https://meteo-data.com/59000.json' 
#Recuperation donnees JSON ATMO et envoi toutes les heures
json_data=requests.get(url).json()
temperature = json_data['temp']
print(temperature)

