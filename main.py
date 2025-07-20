import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TimeField,SelectField
from wtforms.validators import DataRequired
import csv
from dotenv import load_dotenv
load_dotenv("variables.env")


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("my_key")



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Location",validators=[DataRequired()])
    open = StringField("Opening Time",validators=[DataRequired()])
    close = StringField("Closing Time",validators=[DataRequired()])
    coffee = SelectField(
        'Coffee Taste',
        choices=[
            ('', 'Select...'),  # Acts like a placeholder
            ('1', '☕'),
            ('2', '☕☕'),
            ('3', '☕☕☕'),
            ('4',"☕☕☕☕"),
            ('5',"☕☕☕☕☕")
        ],
        validators=[DataRequired()]
    )
    power = SelectField("Power Availability", choices=[("","Select..."),("1","🔌"),("2","🔌🔌"),("3","🔌🔌🔌")],validators=[DataRequired()])
    wifi = SelectField("Power Availability", choices=[("","Select..."),("1","🛜"),("2","🛜🛜"),("3","🛜🛜🛜")],validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
     pass
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
