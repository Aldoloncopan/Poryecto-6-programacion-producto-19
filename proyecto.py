import pandas as pd#importamos la biblioteca pandas
import matplotlib.pyplot as plt#importamos la biblioteca matplotlib
opcion=0
def menu(): #definimos esta funcion para poder hacer uso del  menú de abajo
  opciones = int(input("Menú Principal \n" 
"1. Ver casos activos \n"
"2. Mostrar regiones con mayor y menor taza de contagios\n"
"3. Establecer una métrica de comparación \n"))
  return opciones

while opcion !=3:#se inicia el menu con un while con sus respectivas restricciones e instrucciones
  opcion=menu()
  if opcion==1:
    print("Tarapaca: 01\nAntofagasta: 02\nAtacama:      03\nCoquimbo cod. region: 04\nValparaiso cod. region: 05\nLibertador Gral. Bernardo O’Higgins cod. region: 06\nMaule: 07\nBiobio: 08\nLa Araucania: 09\nLos Lagos: 10\nAysen: 11\nMagallanes y la antartica: 12\nMetropolitana: 13\nLos Rios: 14\nArica y Parinacota: 15\nNuble: 16")
    datos=pd.read_csv('CasosActivosPorComuna.csv',header=0)
    print("INGRESE REGION Y CODIGO DE REGION")
    reg=input('Region: ')
    codr=int(input('Codigo Region: '))
    datos2=datos[['Region','Codigoregion','Comuna']]
    print (datos2[(datos2.Region==reg) & (datos.Codigoregion==codr)])
    print('Ingrese Fechas(Ascendente) y Comuna:')
    fecha=input('Fecha: ')
    fecha2=input('Fecha: ')
    fecha3=input('Fecha: ')
    com=input('Comuna: ')
    datos3=datos[['Region','Comuna', fecha, fecha2,fecha3]]
    print(datos3[(datos3.Region==reg) & (datos.Comuna==com)])
   
    fig, ax = plt.subplots()
    plt.title("Casos Activos")#titulo de la gráfica
    ax.barh([fecha,fecha2,fecha3], [5, 10, 12])#variables representadas en la gráfica
    plt.show()#funcion para mostrar todo lo solicitado

  elif opcion==2:
    datos=pd.read_csv('CasosActivosPorComuna.csv',header=0)
    datos2=datos[['Region','Codigoregion','Comuna']]
    print (datos2[(datos2.Region=='Metropolitana') & (datos.Codigoregion=='13')])
    datos3=datos[['Region','Comuna','2021-07-09']]
    print(datos3[(datos3.Region=='Metropolitana') & (datos.Comuna=='Total')])
    
    datos4=pd.read_csv('CasosActivosPorComuna.csv',header=0)
    datos5=datos4[['Region','Codigoregion','Comuna']]
    print (datos5[(datos5.Region=='Magallanes y la Antartica') & (datos4.Codigoregion=='12')])
    datos6=datos[['Region','Comuna','2021-07-09']]
    print(datos6[(datos6.Region=='Magallanes y la Antartica') & (datos4.Comuna=='Total')])
    fig, ax = plt.subplots()
    plt.ylabel("Casos Activos confirmados(miles)")
    plt.xlabel("Regiones")
    plt.title("Regiones con más y menos densidad casos activos")
    ax.bar(['Metropolitana','Magallanes'], [8780,125])
    plt.show()
