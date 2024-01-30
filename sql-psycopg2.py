""" Module providing a function printing python version."""
import psycopg2


# connect to "chinook" database
connetion = psycopg2.connect(database="chinook", password="12345")


# buid a curso object of the database
cursor = connetion.cursor()


# Query 1 -select all records from the "Artist" table
# cursor.execute('SELECT * FROM "artist"')

# Query 2 -select only the "name" column  from the "Artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# Query 3 -select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# Query 4 -select only "ArtitsId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artistid" = %s', [51])

# Query 5 -select only the albums with "ArtistId" #51 in the "Album" table
# cursor.execute('SELECT * FROM "album" WHERE "artistid" = %s', [51])

# Query 6 -select all tracks where the composer "Queen" from the "track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result(single)
# results =  cursor.fetchone()


# close the connection
connetion.close()


# print rerults
for result in results:
    print(result)
