import time
import signal
import sys
import math 
from math import*
import datetime 
import MySQLdb 
import random
from time import sleep
db = MySQLdb.connect(host="localhost", user="root", passwd="pass", db="TestProjetYES")
curs= db.cursor()
print("Connexion a la BDD reussie")

numero = 4
curs.execute("UPDATE comptage SET cycliste=%i WHERE (id=1)" % (numero))
db.commit()
time.sleep(8)
