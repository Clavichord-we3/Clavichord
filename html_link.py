from flask import Flask, request, render_template
from flaskext.mysql import MySQL
mysql = MySQL()

from music_samples import *

app = Flask(__name__)
mysql.init_app(app)

@app.route('/',methods = ['GET','POST'])
def get_data():
  if request.method == 'POST':
    melody = request.form['Melody']
    bass = request.form['Bass']
    form_data = dict(request.form)
    melody = form_data['Melody'].split(",")
    bass = form_data['Bass']
    play_music(list(map(int, melody)), list(eval(bass)), 0.5)

  return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)