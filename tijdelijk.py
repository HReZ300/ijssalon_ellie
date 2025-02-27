mijn_directory = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5,
}

aanbieding = mijn_directory["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = list(reclame_tekst3)
el = [letter for letter in reclame_tekst4]
woorden = reclame_tekst3.split()

for woord in woorden:
    if len(woord) >= 5:
        print(woord.upper())
    else:
        print(woord.lower())