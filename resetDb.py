import mysql.connector
from settings import *

mycursor = db.cursor()


if input("really? [y/N]").lower() != "y":
    print("canceled")
    exit()
else:
    try:
        mycursor.execute("DROP TABLE tbl_distance")
    finally:
        mycursor.execute("CREATE TABLE tbl_distance (clan varchar(20), walked int UNSIGNED NOT NULL)")
        for i in clanList:
            mycursor.execute("INSERT INTO tbl_distance (clan, walked) VALUES (%s, %s)", (i[0], 0))
        db.commit()

    print("reseted")