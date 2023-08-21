import requests

def precio_en_dolares_bitcoin():
    api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    datos = api.json()
    precio = datos['bpi']['USD']['rate']
    descripcion = datos['bpi']['USD']['description']
    return precio, descripcion

p, d = precio_en_dolares_bitcoin()
print(f'El valor actual del bitcoin en {d} es de ${p}')

def precios_en_monedas_bitcoin():
    api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    datos = api.json()
    us_p = datos['bpi']['USD']['rate']
    us_d = datos['bpi']['USD']['description']
    gbp_p = datos['bpi']['GBP']['rate']
    gbp_d = datos['bpi']['GBP']['description']
    eur_p = datos['bpi']['EUR']['rate']
    eur_d = datos['bpi']['EUR']['description']
    return us_p, us_d, gbp_p, gbp_d, eur_p, eur_d

us_p, us_d, gbp_p, gbp_d, eur_p, eur_d = precios_en_monedas_bitcoin()

print(f'El valor actual del bitcoin en {us_d} es de ${us_p}')
print(f'El valor actual del bitcoin en {gbp_d} es de ${gbp_p}')
print(f'El valor actual del bitcoin en {eur_d} es de ${eur_p}')