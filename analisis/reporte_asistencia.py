from enum import auto
from numpy import fix
import pandas as panda
import csv
from matplotlib import pyplot

datos_estudiantes = panda.read_csv('C:\\Users\\HP\\Documents\\GitHub\\ista-python-curso-2022\\datos\\estudiante.csv')
datos_asistencia = panda.read_csv('C:\\Users\\HP\\Documents\\GitHub\\ista-python-curso-2022\\datos\\asistencia.csv')

asistencias_completas = panda.merge(datos_estudiantes,datos_asistencia)
print(asistencias_completas)

print(asistencias_completas['cedula' == 1939407032])

asistencias_completas[asistencias_completas.cedula == 1939407032].to_csv('C:\\Users\\HP\\Documents\\GitHub\\ista-python-curso-2022\\datos\\reporte_0107308868.csv', index=True)
fig, ax= pyplot.subplots()
ax.scatter(x=[1,2,3,4,5,6,7,8,9,10], y=[])
pyplot.show()
