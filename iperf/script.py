import os
import json
ejemplo_dir = '.'
contenido = os.listdir(ejemplo_dir)
print(contenido)
metrica = []
unidad = []
valores_fichero = []

for fichero in contenido:
	if os.path.isdir(os.path.join(ejemplo_dir, fichero)):
		print(fichero)
		os.chdir(fichero)
		with open("perfkitbenchmarker_results.json") as file:
			for line in file:
				dato = json.loads(line)
				metrica.append(dato['metric'])
				unidad.append(dato['unit'])
				valores_fichero.append(dato['value'])
		print(json.dumps(metrica))
		print(json.dumps(unidad))
		print(json.dumps(valores_fichero))
		os.chdir("..")

	metrica = []
	unidad = []
	valores_fichero = []









