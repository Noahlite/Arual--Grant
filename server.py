
from flask import Flask, render_template,request,redirect

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
from twilio.rest import Client




app = Flask(__name__)
app.secret_key = "helloworld"
Bootstrap(app)


class Form(FlaskForm):
    fname = StringField(label='First Name', validators=[DataRequired()])
    lname = StringField(label='Last Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    phone = IntegerField(label='Phone_number', validators=[DataRequired(),Length(min=10)])
    select = SelectField(label='Help', choices=('Children 👶 ', 'Animals 🐶'))
    text = TextAreaField(label='How much do you wish to donate? ')
    submit = SubmitField(label='Submit')


Twillio_auth = "5d0e5effc0d6ac6525b5179b9c3edd41"
Twillio_ssid = "AC422603a9160fa586da1cbd1e517c03fd"
@app.route('/contact')
def contact():
    return redirect('http://eepurl.com/hMUHeb')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    login_form = Form()
    client= Client(Twillio_ssid,Twillio_auth)

    if request.method == 'POST':
        fname = login_form.fname.data
        lname = login_form.lname.data
        Email = login_form.email.data
        amount = login_form.text.data
        phone = login_form.phone.data
        select = login_form.select.data

        message = f'{fname}-{lname} wants to pay\n' \
                  f'${amount}\n'\
                  f' for {select}\n'\
                  f'{Email}\n' \
                  f'{phone}'

        client.messages.create(from_="+12566175621",
                               to="+18153176218",
                               body=message)





    return render_template('contact.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
