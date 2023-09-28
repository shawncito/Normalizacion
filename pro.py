import re

nombre_archivo = "RPT_RA_11_NOTAS_FINALES_POR_PERIODO 1C 2023 - RPT_RA_11_NOTAS_FINALES_POR_PERIODO 1C 2023"

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
    print("No se encontraron coincidencias.")