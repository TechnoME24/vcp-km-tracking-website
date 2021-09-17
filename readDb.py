from settings import *

mycursor = db.cursor()

def printDb():
    mycursor.execute("SELECT * FROM tbl_distance")
    for i in mycursor:
        print(i)

printDb()