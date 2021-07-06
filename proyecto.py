print("Tarapaca: 01\nAntofagasta: 02\nAtacama: 03\nCoquimbo cod. region: 04\nValparaiso cod. region: 05\nLibertador Gral. Bernardo O’Higgins cod. region: 06\nMaule: 07\nBiobio: 08\nLa Araucania: 09\nLos Lagos: 10\nAysen: 11\nMagallanes y la antartica: 12\nMetropolitana: 13\nLos Rios: 14\nArica y Parinacota: 15\nNuble: 16")
import pandas as pd #Importamos la libreria pandas
datos=pd.read_csv('CasosActivosPorComuna.csv',header=0)
print("INGRESE REGION Y CODIGO DE REGION")
reg=input('Region: ')
codr=int(input('Codigo Region: '))
datos2=datos[['Region','Codigoregion','Comuna']]
print (datos2[(datos2.Region==reg) & (datos.Codigoregion==codr)])
