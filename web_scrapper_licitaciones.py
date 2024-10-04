from datetime import datetime, timedelta
import random
import pandas as pd 

## Textos
EMPRESA_INICIO = "Empresa:"
EMPRESA_FIN = "."

HORAS_INICIO = "Hs. Requeridas por Período:"
HORAS_FIN = "hs"

INGLES_INICIO = "Inglés:"
INGLES_FIN = "D"

PRECIO_BASE_INICIO = "[ $"
PRECIO_BASE_FIN = ";"

PRECIO_TOPE_INICIO = "; $"
PRECIO_TOPE_FIN = "]"

text_scrapped = """

Empresa: Gobierno de Río Negro Hs. Requeridas por Período: 12149 hs Períodos Requeridos: 2 Inglés: NO Descripción: Sistema de Gestión de Lucha contra el Fuego Monto Estimado de Licitación:
[ $910,000 ; $6,740,000 ]
Lic. Pública 3d 22h 33m 30s...


Empresa: Gobierno de Neuquen Hs. Requeridas por Período: 11037 hs Períodos Requeridos: 2 Inglés: NO Descripción: Sistema de Administración del Flujo de Turistas Monto Estimado de Licitación:
[ $780,000 ; $5,320,000 ]
Lic. Pública 2d 22h 33m 30s...


Empresa: Gobierno de Catamarca Hs. Requeridas por Período: 17485 hs Períodos Requeridos: 1 Inglés: 4% Descripción: Sistema de Gestión de Calidad de Servicios Públicos Monto Estimado de Licitación:
[ $630,000 ; $4,420,000 ]
Lic. Pública 3d 22h 33m 30s...


Empresa: Gobierno de Formosa Hs. Requeridas por Período: 15498 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Control de Campañas Electorales Monto Estimado de Licitación:
[ $550,000 ; $3,390,000 ]
Lic. Pública 2d 22h 33m 30s...


Empresa: Gobierno de Tucuman Hs. Requeridas por Período: 13948 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Contabilidad Gubernamental Monto Estimado de Licitación:
[ $510,000 ; $3,100,000 ]
Lic. Pública 3d 22h 33m 30s...


Empresa: Municipalidad de General Alvarado Hs. Requeridas por Período: 11459 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Información Geográfica Monto Estimado de Licitación:
[ $440,000 ; $2,550,000 ]
Lic. Pública 2d 22h 33m 30s...


Empresa: Gobierno de la Provincia de Buenos Aires Hs. Requeridas por Período: 9235 hs Períodos Requeridos: 2 Inglés: NO Descripción: Sistema de Gestión Educativa Monto Estimado de Licitación:
[ $640,000 ; $4,530,000 ]
Lic. Pública 3d 22h 33m 30s...


Empresa: Municipalidad de Bragado Hs. Requeridas por Período: 9563 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Trámites a Distancia Monto Estimado de Licitación:
[ $360,000 ; $2,700,000 ]
Lic. Pública 2d 22h 33m 30s...


Empresa: Municipalidad de Tornquist Hs. Requeridas por Período: 14864 hs Períodos Requeridos: 1 Inglés: 8% Descripción: Sistema de Control de Servicios Bancariosl Monto Estimado de Licitación:
[ $580,000 ; $3,500,000 ]
Lic. Pública 3d 22h 33m 30s...


Empresa: Gobierno de San Luis Hs. Requeridas por Período: 9560 hs Períodos Requeridos: 1 Inglés: 18% Descripción: Sistema de Gestión de Recursos Naturales Monto Estimado de Licitación:
[ $370,000 ; $2,590,000 ]
Lic. Privada 2d 22h 33m 30s...


Empresa: Danske Bank Hs. Requeridas por Período: 7046 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Administración de Perfiles de Clientes Monto Estimado de Licitación:
[ $370,000 ; $1,580,000 ]
Lic. Privada 3d 22h 33m 30s...


Empresa: Avion Express Hs. Requeridas por Período: 9248 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Pago Electrónico Monto Estimado de Licitación:
[ $550,000 ; $2,510,000 ]
Lic. Privada 2d 22h 33m 30s...


Empresa: Small Planet Airlines Hs. Requeridas por Período: 10968 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Detección de Spam y Phishing Monto Estimado de Licitación:
[ $600,000 ; $2,840,000 ]
Lic. Privada 3d 22h 33m 30s...


Empresa: Equinor Hs. Requeridas por Período: 8905 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Autogestión de Proveedores Monto Estimado de Licitación:
[ $570,000 ; $2,490,000 ]
Lic. Privada 2d 22h 33m 30s...


Empresa: Pretroleum Geo Services Hs. Requeridas por Período: 7090 hs Períodos Requeridos: 1 Inglés: 10% Descripción: Sistema Medidor de Temperatura Corporal Monto Estimado de Licitación:
[ $510,000 ; $2,040,000 ]
Lic. Privada 3d 22h 33m 30s...


Empresa: Buffalo Wings Hs. Requeridas por Período: 7323 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Tickets Monto Estimado de Licitación:
[ $380,000 ; $1,530,000 ]
Lic. Privada 2d 22h 33m 30s...


Empresa: Capri Holdings Hs. Requeridas por Período: 8035 hs Períodos Requeridos: 2 Inglés: NO Descripción: Sistema de Pago Electrónico Monto Estimado de Licitación:
[ $860,000 ; $3,340,000 ]
Lic. Privada 3d 22h 33m 30s...


Empresa: NTT Data Hs. Requeridas por Período: 11695 hs Períodos Requeridos: 1 Inglés: 10% Descripción: Sistema de Análisis de Indicador de Felicidad Monto Estimado de Licitación:
[ $800,000 ; $3,200,000 ]
Lic. Privada 2d 22h 33m 30s...


Empresa: Keystone Hs. Requeridas por Período: 8549 hs Períodos Requeridos: 1 Inglés: 35% Descripción: Implementación de Data Warehouse para el Tratamiento de Big Data Monto Estimado de Licitación:
[ $770,000 ; $3,240,000 ]
Proyecto ...


Empresa: UTN BA Hs. Requeridas por Período: 8220 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema de Aulas Virtuales Paga: $940,000
Proyecto ...


Empresa: Trintech Hs. Requeridas por Período: 3315 hs Períodos Requeridos: 1 Inglés: NO Descripción: Sistema Cuantificación y Optimización de Rendimiento del Personal Paga: $410,000
Proyecto ...


Empresa: Nuxeo Hs. Requeridas por Período: 4044 hs Períodos Requeridos: 1 Inglés: 40% Descripción: Sistema de Análisis de Customer Experience Paga: $540,000
Proyecto ...


Empresa: LTI Hs. Requeridas por Período: 6207 hs Períodos Requeridos: 1 Inglés: 35% Descripción: Sistema de Reportes con Big Data Paga: $870,000
"""


def main():
    lineas = text_scrapped.splitlines()
    lineas_sin_vacias = [linea for linea in lineas if linea.strip()]

    print("Start script, name of lines: ", len(lineas))
    global empresa, horas, ingles, precio_min, precio_max, tipo_licitacion
    
    for numero, linea in enumerate(lineas_sin_vacias, start=1):
        if esRestoUnoDeTres(num=numero):
            empresa = extrarDato(linea, EMPRESA_INICIO, EMPRESA_FIN)
            
            horas = extrarDato(linea, HORAS_INICIO, HORAS_FIN)
            ingles = extrarDato(linea, INGLES_INICIO, INGLES_FIN)   
        
        elif esRestoDosDeTres(num = numero):
            precio_min = extrarDato(linea, PRECIO_BASE_INICIO, PRECIO_BASE_FIN)
            precio_max = extrarDato(linea, PRECIO_TOPE_INICIO, PRECIO_TOPE_FIN)   
        
        else :
            tipo_licitacion = linea[0:13]
            tipo_licitacion =  parsearTipoLicitacion(tipo_licitacion)
            print ( ";".join([empresa, horas, ingles, precio_min.replace(',',""), precio_max.replace(',',""), tipo_licitacion]) )
         
         
def parsearNumero(anString):
    return anString         

def parsearTipoLicitacion(tipo_licitacion):
    if (tipo_licitacion == "Lic. Pública "):
        return "Pública"
    elif (tipo_licitacion == "Lic. Privada "):
        return "Privada"
    elif (tipo_licitacion == "Proyecto ..."): 
        return "Proyecto"
    else : 
        return "NoMatch"

def extrarDato(parrafo, word_inicio, word_fin):
    partes = parrafo.split(word_inicio, 1)

    if len(partes) > 1:
        texto_intermedio = partes[1].split(word_fin, 1)[0]
        return texto_intermedio
    else:
        return



def esRestoUnoDeTres(num):
    return num % 3 == 1


def esRestoDosDeTres(num):
    return num % 3 == 2

def esMultiploDeTres(num):
    return num % 3 == 0



if __name__ == '__main__':
    main()