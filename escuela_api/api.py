from fileinput import filename
import json
from flask import Flask, jsonify, request
import csv

application = Flask(__name__)

@application.route('/')
def inicio():
    return "Marco Geovanny Cuzco Villa M5B"

@application.route('/lista_estudiantes',methods=['GET'])
def listado():
    with open(file='C:\\Users\\HP\\Documents\\GitHub\\ista-python-curso-2022\\datos\\estudiante.csv') as f:
        reader = csv.reader(f)
        next(reader)
        listaEst = []
        for fila in reader:
            listaEst.append({
                'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
            })
    return jsonify(sorted(listaEst,key=lambda a: a['primer_apellido']))
    
    
@application.route('/registroasistencia',methods=['POST'])
def ingresarDatos():
    if request.method=='POST':
        with open('C:\\Users\\HP\\Documents\\GitHub\\ista-python-curso-2022\\datos\\asistencia.csv', 'a', newline='') as d:
            escribir = csv.writer(d,delimiter=',')
            escribir.writerow([request.form['cedula'],request.form['materia'],request.form['fecha_anio'],request.form['fecha_mes'],request.form['fecha_dia']])
        return "Registro Creado"
