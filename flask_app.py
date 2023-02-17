import os

from flask import Flask, request, url_for, redirect, render_template, flash
import requests

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/flask_portfolio")
def flask_portfolio():
    return render_template('portfolio.html')

@app.route("/contact_form", methods=["POST", "GET"])
def contact_form():
    if request.method == "POST":
        contact_name = request.form.get("fullname")
        contact_email = request.form.get("email")
        contact_phone = request.form.get("phone")
        contact_message = request.form.get("message")
        response = requests.post('https://bebemail.edjeware.com/emails', json={"to": os.getenv("WEB_MASTER_EMAIL_ADDRESS")})
        response.raise_for_status()

        flash(f"{contact_name}, {contact_email}, {contact_phone}, {contact_message}")
        return redirect(url_for("form_data"))
    else:
        return render_template('contact_form.html')



@app.route("/success")
def form_data():
    return render_template('form_success.html')

@app.route('/<name>')
def sleeper(name):
    return f'Hello, {name}'

@app.route('/admin')
def admin(name=None):
        return render_template('admin.html', name=name)

@app.route("/sleeping")
def sleep(name='eve'):
    return render_template('sleeping.html', name=name)


if __name__=="__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/


#{{ url_for('static', filename='')}}