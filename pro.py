import re
import os
import glob
import pandas

def encontrar_perido(nombre_archivo):
        patron = r'(\d+)C ?(\d+)'

        # Busca la primera coincidencia en el nombre del archivo
        coincidencia = re.search(patron, nombre_archivo)

        # Verificamos si se encontró una coincidencia
        if coincidencia:
            numero_despues_de_C = coincidencia.group(1)
            numero_antes_de_C = coincidencia.group(2)
            numero1 = numero_antes_de_C + "-" + numero_despues_de_C
            print("Número:", numero1)
            #procesar_archivo_RPT_11(numero1, archivo_salida,)
            return numero1

def encontrar_anio(nombre_archivo):
        patron_anio = r'(\d{4})[^0-9]'

        # Busca el año en el nombre del archivo
        patron_quinto_digito = r'(\d)(\d{4})'
        # Busca el año en el nombre del archivo
        coincidencia_anio = re.search(patron_anio, nombre_archivo)
        # Busca el quinto dígito en el nombre del archivo
        coincidencia_quinto_digito = re.search(patron_quinto_digito, nombre_archivo)
        # Verifica si se encontraron coincidencias
        if coincidencia_anio and coincidencia_quinto_digito:
            anio = coincidencia_anio.group(1)
            quinto_digito = coincidencia_quinto_digito.group(1)
            numero2 = anio+'-'+quinto_digito
            print("Número:", numero2)
            return numero2


'''nombre_archivo = "RPT_RA_11_NOTAS_FINALES_POR_PERIODO 1C 2023 - RPT_RA_11_NOTAS_FINALES_POR_PERIODO 1C 2023"

# Patrón de expresión regular para encontrar números antes y después de "C" con un espacio opcional
patron = r'(\d+)C ?(\d+)'

# Busca la primera coincidencia en el nombre del archivo
coincidencia = re.search(patron, nombre_archivo)

# Verificamos si se encontró una coincidencia
if coincidencia:
    numero_despues_de_C = coincidencia.group(1)
    numero_antes_de_C = coincidencia.group(2)
    numero = numero_antes_de_C + "-" + numero_despues_de_C
    print("Número:", numero)
else:
    print("No se encontraron coincidencias.")'''