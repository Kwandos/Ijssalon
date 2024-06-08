# Importeer benodigde functies en variabelen
from helper import som
from presentatie import presenteer
import csv

# Definieer de inkomsten dictionary
inkomsten = {
    'Aardbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750
}

# Bereken de totale inkomsten
totaal_inkomsten = som(inkomsten)

# Presenteer de inkomsten
presenteer(inkomsten, totaal_inkomsten)

# Schrijf inkomsten naar een CSV-bestand
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])
