from flask import Flask, render_template
import sqlite3

con = sqlite3.connect("tutorial.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cars( year, model)")
cur.execute("INSERT INTO cars VALUES ('2020','Mazda 3'),('2021','Ford focus')")
con.commit()
# for i in cur.execute("select * from cars"):
#    print(i)

app = Flask(__name__)


@app.route("/")
def hello_world():
   cars = []
   for i in cur.execute("select * from cars"):
      print(i)
      cars.append(i)
   return render_template("cars.html",cars=cars)

@app.route("/addcar")
def add_car():
   model = input("model")
   year = input("year")
   cur.execute(f"INSERT INTO cars VALUES ('{year}', '{model}');")
   con.commit()
   return "<h1>Added succesfuly!</h1>"
   
# @app.route("/addcar")
# def add_car():
#    model = input("model")
#    year = input("year")
#    cur.execute("INSERT INTO cars VALUES ({model}, {year});")
#    con.commit()
#    return "<h1>Added succesfuly!</h1>"



# app.run(debug=True)c