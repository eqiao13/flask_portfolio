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
    error = None
    if request.method == "POST":
        contact_name = request.form.get("name")
        contact_email = request.form.get("email")
        contact_phone = request.form.get("phone")
        contact_message = request.form.get("message")

        #checking to see if they filled out all the fields in the form
        if contact_name is "" or contact_email is "" or contact_phone is "" or contact_message is "":
            return redirect(url_for('form_fail'))
        else:
            #connecting to the email server
            response = requests.post('https://bebemail.edjeware.com/', headers={"API-ID": os.getenv("BEBEMAIL_API_ID"), "API-SECRET": os.getenv("BEBEMAIL_API_SECRET")}, json={"to": os.getenv("WEB_MASTER_EMAIL_ADDRESS"), "subject": "A message for the avatar", "body": f"You got an email from {contact_name}\nEmail: {contact_email}\nPhone number: {contact_phone}\nMessage: {contact_message}"})
            #breakpoint()

            #flashing message if it send or error and display those messages in a new link HTML page
            status = response.raise_for_status()
            if status == 200 or 202:
                flash(f"You sent\n\n From: {contact_name}\n\n Email: {contact_email}\n\n Phone: {contact_phone}\n\n Message:{contact_message}")
                return redirect(url_for("form_success"))
            else:
                flash("Something went wrong, your email didn't go through.", 'error')
                return redirect(url_for('form_fail'))
    else:
        return render_template('contact_form.html')



@app.route("/success")
def form_success():
    return render_template('form_success.html')

@app.route("/failed")
def form_fail():
    return render_template('form_fail.html')

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