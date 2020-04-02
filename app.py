from flask import Flask, render_template, url_for, redirect, request, flash
from forms import EmailInput
from main import valid_email

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cb8631d5b4cf1a13f4355798845a93'

@app.route('/hello')
def hello():
    return render_template('%s.html' % 'flashmessage')

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = EmailInput(request.form)
    if form.validate_on_submit():
        email_address = request.form['email']
        if (valid_email(email_address)):
            return redirect(url_for('valid', email_address=email_address))
        return redirect(url_for('invalid', email_address=email_address))

    return render_template('%s.html' % "emailform", form=form)

@app.route('/valid=<email_address>')
def valid(email_address):
    return '%s is a valid member' % email_address

@app.route('/invalid=<email_address>')
def invalid(email_address):
    return '%s is not a valid member' % email_address


if __name__ == "__main__":
    app.run(debug=True)



