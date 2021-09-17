import mysql.connector

#----------database settings----------
db = mysql.connector.connect(
    host="localhost",
    port="3333",
    user="phillip",
    passwd="root",
    database="testdatabase"
)

clanList = [("wölflinge","Wölflinge"),
            ("benjamine", "Benjamine"),
            ("kangurus", "Kangurus"),
            ("steinbock", "Steinbock"),
            ("koala", "Koala"),
            ("panda", "Panda"),
            ("skorpion", "Skorpion"),
            ("gepard", "Gepart"),
            ("luchs", "Luchs"),
            ("mammut", "Mammut"),
            ("lupo", "Lupo"),
            ("schildkröten", "Schildkröten"),
            ("leopard", "Leopard"),
            ("jaguar", "Jaguar"),
            ("inactive", "inaktieve Sippe")]

#----------website settings----------
passwd = "123"