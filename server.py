
from flask import Flask, render_template,request,redirect,url_for

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
from pymongo import MongoClient



app = Flask(__name__)
app.secret_key = "helloworld"
Bootstrap(app)


class Form(FlaskForm):
    fname = StringField(label='First Name', validators=[DataRequired()])
    lname = StringField(label='Last Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    phone = IntegerField(label='Phone_number', validators=[DataRequired()])
    select = SelectField(label='Help', choices=('Children 👶 ', 'Animals 🐶'))
    text = IntegerField(label='How much do you wish to donate? ',validators=[DataRequired()])
    submit = SubmitField(label='Submit')


client =MongoClient("mongodb+srv://test:test@cluster0.gvn73.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('charity_db')
records = db.charity_records
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
    # client= Client(Twillio_ssid,Twillio_auth)

    if login_form.validate_on_submit():
        fname = login_form.fname.data
        lname = login_form.lname.data
        Email = login_form.email.data
        amount = login_form.text.data
        phone = login_form.phone.data
        select = login_form.select.data

        charity_giver = {'fname':fname,
                         'lname':lname,
                         'email':Email,
                         'phone':phone,
                         'select':amount,
                         'amount':select}
        records.insert_one(charity_giver)
        return redirect(url_for('home'))
    return render_template('contact.html', form=login_form)


if __name__ == "__main__":
    app.run()
