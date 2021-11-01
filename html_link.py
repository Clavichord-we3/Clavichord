from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql = MySQL()

from music_samples import *

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'weprojectdb'
app.config['MYSQL_DATABASE_host'] = '127.0.0.1:3306'
mysql.init_app(app)

@app.route('/',methods = ['GET','POST'])
def get_data():
  if request.method == 'POST':
    melody = request.form['Melody']
    bass = request.form['Bass']
    play_music(list(melody), list(bass), 0.5)
    print(list(melody))
    print(list(bass))
    connection = mysql.get_db()
    cursor = connection.cursor()
    query = "INSERT INTO store_inputs(Melody, Bass) VALUES(%s,%s)"
    cursor.execute(query,(melody, bass))
    connection.commit()

  return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)
#add-content-to-html-link
