from flask import Flask
from flask import render_template
from flask import request
import database as dbl

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('formular.html')

@app.route("/modtag_data", methods=['POST'])
def modtag():
    modtaget_navn = request.form['navn']
    modtaget_mail = request.form['email']
    dbl.new_user(modtaget_navn, modtaget_mail)
    return render_template("vis.html", navn = modtaget_navn, email = modtaget_mail)

@app.route('/admin')
def admin():
    database_return = dbl.show_users(False, True)
    return render_template('admin.html', users= database_return)

if __name__ == "__main__":
    app.run(debug=True)
