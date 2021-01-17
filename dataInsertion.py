import csv
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

a_file = open("movies_metadata.csv", encoding="utf8")
rows = csv.reader(a_file)
#name,adult,budget,genres,homepage,original_language,production_companies,release_date,revenue,rating
cur.executemany("INSERT INTO movie_model (name,adult,budget,genres,homepage,original_language,production_companies,release_date,revenue,rating) VALUES (?,?,?,?,?,?,?,?,?,?)", rows)

cur.execute("SELECT * FROM movie_model")
con.commit()
con.close()