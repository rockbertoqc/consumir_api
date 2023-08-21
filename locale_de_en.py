import locale
from datetime import datetime
import calendar

# Configuración regional 'de_DE'
locale.setlocale(locale.LC_ALL, 'de_DE')
formatted_number_de = locale.format_string("%.2f", 12345.67)
formatted_date_de = datetime.now().strftime("%A, %d %B %Y")

# Configuración regional 'en_US'
locale.setlocale(locale.LC_ALL, 'en_US')
formatted_number_en = locale.format_string("%.2f", 12345.67)
formatted_date_en = datetime.now().strftime("%A, %d %B %Y")

print("Configuración regional 'de_DE':")
print("Número formateado:", formatted_number_de)
print("Fecha formateada:", formatted_date_de)

print("\nConfiguración regional 'en_US':")
print("Número formateado:", formatted_number_en)
print("Fecha formateada:", formatted_date_en)

# Configuración regional 'es_MX'
locale.setlocale(locale.LC_ALL, 'es_MX')
formatted_number_mx = locale.format_string("%.2f", 12345.67)
formatted_date_mx = datetime.now().strftime("%A, %d de %B de %Y")

print("Configuración regional 'es_MX':")
print("Número formateado:", formatted_number_mx)
print("Fecha formateada:", formatted_date_mx)

# Obtener el nombre del mes y el año actual
mes_actual = 8  # Agosto
año_actual = 2023

# Crear un objeto de calendario para el mes y año especificados
cal = calendar.monthcalendar(año_actual, mes_actual)

# Obtener el nombre del mes en el contexto regional
nombre_mes = calendar.month_name[mes_actual]

# Imprimir el calendario del mes
print(f"Calendario de {nombre_mes} {año_actual}:\n")
print("L  M  X  J  V  S  D")

for semana in cal:
    semana_str = " ".join(str(dia) if dia != 0 else "  " for dia in semana)
    print(semana_str)
