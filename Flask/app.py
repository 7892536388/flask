from flask import Flask, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'any-secret-key'

class SimpleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash(f'Form submitted! Name: {form.name.data}, Email: {form.email.data}', 'success')
        return redirect('/')
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
