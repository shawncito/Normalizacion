import os
import glob
from transformar_csv_rpt_ra_11_notas_finales_por_periodo import procesar_archivo_RPT_11 as procesar_archivo_RPT_11
from transformar_xlsx_rpt_rg_04_estudiantes_institucion import procesar_archivo_RPT_RG_04 as procesar_archivo_RPT_RG_04
from transformar_xlsx_rpt_rg_05_estado_estudiantes import procesar_archivo_xlsx as procesar_archivo_RPT_RG_05
from Limpiar_RPT_RG_01_Estudiantes import precesar_archivo_RPT_RG_01_estudiantes as precesar_archivo_RPT_RG_01_estudiantes
from Limpiar_RPT_RM_03_EstudiantesNiveles import procesar_archivo_RPT_RM_03_Estudiantes as procesar_archivo_RPT_RM_03_Estudiantes



# Directorio donde se encuentran los archivos CSV y XLSX
directorio_entrada = "./data"

# Patrón de nombre de archivo CSV y XLSX que deseas buscar
patron_nombre_archivo_csv = "RPT_RA_11_NOTAS_FINALES_POR_PERIODO*.csv"
patron_nombre_archivo_xlsx = "RPT_RG_04_EstudiantesInstitucion.xlsx"
patron_nombre_archivo_xlsx_rg_05 = "RPT_RG_05_EstadoEstudiantes.xlsx"
patron_nombre_archivo_csv_rg_01 = "RPT_RG_01_Estudiantes.csv"
patron_nombre_archivo_csv_rm_03 = "RPT_RM_03_EstudiantesNiveles.csv"


# Utilizar glob para obtener la lista de archivos que coinciden con el patrón CSV
archivos_csv = glob.glob(os.path.join(directorio_entrada, patron_nombre_archivo_csv))

# Utilizar glob para buscar el archivo XLSX
archivo_xlsx = glob.glob(os.path.join(directorio_entrada, patron_nombre_archivo_xlsx))

# Utilizar glob para buscar el archivo XLSX de RG_05
archivo_xlsx_rg_05 = glob.glob(os.path.join(directorio_entrada, patron_nombre_archivo_xlsx_rg_05))

# Utilizar glob para buscar el archivo CSV de RG_01
archivo_csv_rg_01 = glob.glob(os.path.join(directorio_entrada, patron_nombre_archivo_csv_rg_01))

# Utilizar glob para buscar el archivo CSV de RM_03
archivo_csv_rm_03 = glob.glob(os.path.join(directorio_entrada, patron_nombre_archivo_csv_rm_03))

def RPT_RA_11_NOTAS_FINALES_POR_PERIODO(archivos_csv):
        
    # Procesar archivos CSV
    for archivo_csv in archivos_csv:
        # Construir el nombre de archivo de salida
        nombre_archivo = os.path.basename(archivo_csv)
        archivo_salida = os.path.join("DATA_NORMALIZADA", nombre_archivo)

        # Procesar el archivo CSV
        procesar_archivo_RPT_11(archivo_csv, archivo_salida)
        print("Se ha procesado el archivo: " + archivo_csv)

def RPT_RG_04_EstudiantesInstitucion(archivo_xlsx):
    # Procesar archivo XLSX si existe
    if archivo_xlsx:
        archivo_xlsx = archivo_xlsx[0]  # Tomar el primer archivo XLSX si hay varios
        # Construir el nombre de archivo de salida
        nombre_archivo = os.path.basename(archivo_xlsx)
        archivo_salida = os.path.join("DATA_NORMALIZADA", nombre_archivo[:-5] + "_normalizado.csv")  # Cambiamos la extensión a CSV

        # Procesar el archivo XLSX
        procesar_archivo_RPT_RG_04(archivo_xlsx, archivo_salida)
        print("Se ha procesado el archivo: " + archivo_xlsx)

def RPT_RG_05_EstadoEstudiantes(archivo_xlsx_rg_05):
    # Procesar archivo XLSX de RG_05 si existe
    if archivo_xlsx_rg_05:
        archivo_xlsx_rg_05 = archivo_xlsx_rg_05[0]  # Tomar el primer archivo XLSX si hay varios
        # Construir el nombre de archivo de salida
        nombre_archivo = os.path.basename(archivo_xlsx_rg_05)
        archivo_salida = os.path.join("DATA_NORMALIZADA", nombre_archivo[:-5] + "_normalizado.csv")  # Cambiamos la extensión a CSV

        # Procesar el archivo XLSX de RG_05
        procesar_archivo_RPT_RG_05(archivo_xlsx_rg_05, archivo_salida)
        print("Se ha procesado el archivo: " + archivo_xlsx_rg_05)


def RPT_RG_01_Estudiantes(archivo_csv_rg_01):
        # Procesar archivo CSV de RG_01 si existe
    if archivo_csv_rg_01:
        archivo_csv_rg_01 = archivo_csv_rg_01[0]  # Tomar el primer archivo CSV si hay varios
        # Construir el nombre de archivo de salida
        nombre_archivo = os.path.basename(archivo_csv_rg_01)
        archivo_salida = os.path.join("DATA_NORMALIZADA", nombre_archivo[:-4] + "_normalizado.csv")  # Cambiamos la extensión a CSV

        # Procesar el archivo CSV de RG_01
        precesar_archivo_RPT_RG_01_estudiantes(archivo_csv_rg_01, archivo_salida)
        print("Se ha procesado el archivo: " + archivo_csv_rg_01)

def RPT_RM_03_EstudiantesNiveles(archivo_csv_rm_03):
    # Procesar archivo CSV de RM_03 si existe
    if archivo_csv_rm_03:
        archivo_csv_rm_03 = archivo_csv_rm_03[0]  # Tomar el primer archivo CSV si hay varios
        # Construir el nombre de archivo de salida
        nombre_archivo = os.path.basename(archivo_csv_rm_03)
        archivo_salida = os.path.join("DATA_NORMALIZADA", nombre_archivo[:-4] + "_normalizado.csv")  # Cambiamos la extensión a CSV

        # Procesar el archivo CSV de RM_03
        procesar_archivo_RPT_RM_03_Estudiantes(archivo_csv_rm_03, archivo_salida)
        print("Se ha procesado el archivo: " + archivo_csv_rm_03)
#def mensaje():
 #    print("Se han procesado los archivos")
# Mostrar mensaje si no se encontraron archivos
#if not archivos_csv and not archivo_xlsx and not archivo_xlsx_rg_05:
   # print("No se encontraron archivos RPT_RA_11_NOTAS_FINALES_POR_PERIODO, RPT_RG_04_EstudiantesInstitucion ni RPT_RG_05_EstadoEstudiantes en el directorio de entrada.")


#menu
def menu():
    print("Bienvenido al programa de normalización de datos")
    print("Seleccione una opción")
    print("1. RPT_RA_11_NOTAS_FINALES_POR_PERIODO")
    print("2. RPT_RG_04_EstudiantesInstitucion")
    print("3. RPT_RG_05_EstadoEstudiantes")
    print("4. RPT_RG_01_Estudiantes")
    print("5. RPT_RM_03_EstudiantesNiveles")
    print("6. Todo(Cuidado)")
    print("7. Salir")
    case = int(input("Ingrese una opción: "))
    switch(case)


#switch case        


def switch(case):
    if case == 1:
        RPT_RA_11_NOTAS_FINALES_POR_PERIODO(archivos_csv)
    elif case == 2:
        RPT_RG_04_EstudiantesInstitucion(archivo_xlsx)
    elif case == 3:
        RPT_RG_05_EstadoEstudiantes(archivo_xlsx_rg_05)
    elif case == 4:
        RPT_RG_01_Estudiantes(archivo_csv_rg_01)
    elif case == 5:
        RPT_RM_03_EstudiantesNiveles(archivo_csv_rm_03)
    elif case == 6:
        RPT_RA_11_NOTAS_FINALES_POR_PERIODO(archivos_csv)
        RPT_RG_04_EstudiantesInstitucion(archivo_xlsx)
        RPT_RG_05_EstadoEstudiantes(archivo_xlsx_rg_05)
        RPT_RG_01_Estudiantes(archivo_csv_rg_01)
        RPT_RM_03_EstudiantesNiveles(archivo_csv_rm_03)
    elif case == 7:
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida")
    menu()
menu()