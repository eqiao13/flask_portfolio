from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/flask_portfolio")
def flask_portfolio():
    return render_template('portfolio.html')

@app.route('/<name>')
def sleeper(name):
    return f'Hello, {name}'

@app.route('/admin')
def admin(name=None):
        return render_template('admin.html', name=name)

@app.route("/sleeping")
def sleep(name='eve'):
    return render_template('sleeping.html', name=name)

#app.run(port=5001)
#http://127.0.0.1:5001