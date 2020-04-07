from flask import Flask, render_template, url_for, redirect, request
from forms import EmailInput
from main import valid_email

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cb8631d5b4cf1a13f4355798845a93'

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = EmailInput(request.form)
    if form.validate_on_submit():
        email_address = request.form['email']
        if(valid_email(email_address)):
            return redirect(url_for('valid', email=email_address))
        return redirect(url_for('invalid', email=email_address))
    return render_template('%s.html' % "emailform", form=form)

@app.route('/valid<email>')
def valid(email):
    return render_template('%s.html' % 'valid', email=email)

@app.route('/invalid<email>')
def invalid(email):
    return render_template('%s.html' % 'invalid', email=email)


if __name__ == "__main__":
    app.run(debug=True)



