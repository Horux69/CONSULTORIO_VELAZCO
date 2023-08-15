from flask import Flask, render_template

programa = Flask(__name__)

@programa.route('/')
def index():
    return render_template("login.html")

if __name__ == '__main__':
    programa.run(host='0.0.0.0', debug=True, port='8080')