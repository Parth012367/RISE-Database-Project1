# app.py

from flask import Flask, render_template, redirect, url_for, request
from config import Config
from models import db, Patient
from forms import PatientForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    form = PatientForm()
    if form.validate_on_submit():
        new_patient = Patient(
            name=form.name.data,
            age=form.age.data,
            disease=form.disease.data
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_patient.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    form = PatientForm(obj=patient)
    if form.validate_on_submit():
        patient.name = form.name.data
        patient.age = form.age.data
        patient.disease = form.disease.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_patient.html', form=form)

@app.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
