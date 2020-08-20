from flask import Flask, render_template, request
import chargen

app=Flask(__name__)

@app.route('/chargen')
def index():
    return render_template('index.html')

@app.route('/chargen', methods=['POST'])
def input_from_user():
    race = request.form['race']
    number = int(request.form['number'])
    outputChars = []
    for _ in range(number):
        char = chargen.Character(race)
        outputChars.append(char.reportChar())
    
    return render_template("index.html", characters=outputChars)