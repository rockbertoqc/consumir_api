import requests # Biblioteca para hacer peticiones a api
import locale # Biblioteca para formatos de huso horario y cantidades
locale.setlocale(locale.LC_ALL, 'en_US') # Importa el formato de la cantidad


r = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population') # Hacemos la petición get para la ruta de la api
datos = r.json() # Esto vuelca todos los datos de la api en la variable datos

y = datos['data']

for get_y in y:
    poblacion = get_y['Population']
    anio = get_y['Year']
    formateado = locale.format_string("%d", poblacion, grouping=True) # Da formato a la cantidad (000, 000)
    print (f'La población en Estados Unidos era de {formateado} habitantes en el año {anio}')