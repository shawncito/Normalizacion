import pandas as pd
import os
import re

# Definir funciones para eliminar columnas
def eliminar_columnas(df, columnas):
    return df.drop(columns=columnas, axis=1)

# Definir funciones para renombrar columnas
def renombrar_columna(df, columna_original, nuevo_nombre):
    return df.rename(columns={columna_original: nuevo_nombre})

#agraegar nuevo columla al inicio 
def agregar_columna_inicio(df, columna, valor):
    df.insert(0, columna, valor)
    return df

def encontrar_perido(nombre_archivo, archivo_salida):
        patron = r'(\d+)C ?(\d+)'

        # Busca la primera coincidencia en el nombre del archivo
        coincidencia = re.search(patron, nombre_archivo)

        # Verificamos si se encontró una coincidencia
        if coincidencia:
            numero_despues_de_C = coincidencia.group(1)
            numero_antes_de_C = coincidencia.group(2)
            numero1 = numero_antes_de_C + "-" + numero_despues_de_C
            print("Número:", numero1)
            procesar_archivo_RPT_11(numero1, archivo_salida)
            #procesar_archivo_RPT_11(numero1, archivo_salida,)
            return numero1

def encontrar_anio(nombre_archivo, archivo_salida):
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
            procesar_archivo_RPT_11(numero2, archivo_salida)
            return numero2



# Definir función para procesar un archivo CSV
def procesar_archivo_RPT_11(archivo_entrada, archivo_salida, numero):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_entrada)

    # Utilizar una expresión regular para buscar números al final del nombre del archivo
    df['Periodo'] = numero
    
    # Columnas a eliminar
    columnas_a_eliminar = ['textbox16', 'textbox22', 'textbox47', 'textbox36',
                           'textbox40', 'textbox49', 'textbox51', 'textbox53',
                           'textbox55', 'GRPSTN', 'textbox6']

    # Eliminar las columnas no deseadas
    df = eliminar_columnas(df, columnas_a_eliminar)
    #valor de la columna textbox56
    p = df['textbox56'].iloc[0]

    # Agregar columna Tipo
    #df = agregar_columna_inicio(df, 'Periodo', p)
    # Renombrar columnas
    renombrar_dict = {
        'textbox32': 'Carrera',
        'textbox46': 'Materia',
        'textbox48': 'CodClass',
        'textbox50': 'Grupo',
        'textbox52': 'Creditos',
        'textbox54': 'CodProf',
        'textbox56': 'Cuatrimestre',
        'CLINAM'   : 'Nombre',
        'GRPCUN'   : "Id-Estudiante",
        'GRPNTA'   : 'Nota',
    }

    #limpiar las columna 
    df.loc[df['textbox32'] == int, 'textbox32'] = None
    df.loc[df['textbox46'] == int, 'textbox46'] = None
    df.loc[df['textbox48'] == int, 'Nombre'] = None
    df.loc[df['textbox50'] == str, 'textbox50'] = None
    df.loc[df['textbox52'] == str, 'textbox52'] = None
    df.loc[df['textbox54'] == 0, 'textbox54'] = None
    df.loc[df['textbox56'] == str, 'textbox56'] = None
    df.loc[df['CLINAM'] == int, 'CLINAM'] = None
    df.loc[df['CLINAM'] == 0, 'CLINAM'] = None
    df.loc[df['GRPCUN'] == str, 'GRPCUN'] = None
    df.loc[df['GRPNTA'] == str, 'GRPNTA'] = None
    df.loc[df['GRPNTA'] == 0, 'GRPNTA'] = None
    #df.loc[df['GRPNTA'] == None, 'GRPNTA'] = "nada"
    
    #procesar(nombre_archivo)

    # Eliminar la columna existente "Periodo"
    df.drop(columns=['Periodo'], inplace=True)

    # Agregar la nueva columna "Periodo" al inicio
    df.insert(0, 'Periodo', p)

    for columna_original, nuevo_nombre in renombrar_dict.items():
        df = renombrar_columna(df, columna_original, nuevo_nombre)

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv(archivo_salida, index=False)