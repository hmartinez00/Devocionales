import json

ruta_archivo_json = 'settings/requirements/requirements.json'
installed_packages = 'settings/requirements/installed_packages.txt'
requirements = 'requirements.txt'

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)
keys = list(datos_json.keys())

packages = []
with open(installed_packages, encoding='utf-8') as f:
    for line in f:
        packages.append(line)




string = ''
with open(requirements, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

string = ''
for i in keys:
    for j in packages:
        if i.replace('_', '-') in j:
            string = string + j

with open(requirements, 'w', encoding='utf-8') as f:
    f.write(string)
f.close()

print(string)