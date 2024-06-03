# Dictionary met prijzen van verschillende ijssoorten
prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocolade': 5
}

# Bereken de aanbieding voor vanille-ijs
aanbieding = prijzen['vanille'] * 0.8

# Maak een reclame tekst met de aanbiedingsprijs
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts €{aanbieding:.2f}"

# Creëer een nieuwe versie van de reclametekst tot aan de eerste '0' na de komma
reclame_tekst2 = reclame_tekst[:reclame_tekst.index('.') + 3]

# Maak de tekst in hoofdletters voor het spandoek
reclame_tekst3 = reclame_tekst2.upper()

# Splits de tekst in een lijst van woorden
reclame_tekst4 = reclame_tekst3.split()

# Print de woorden onder elkaar, past de weergave aan afhankelijk van de lengte van elk woord
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
