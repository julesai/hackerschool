import spacy
import numpy
import random

# wir laden ein deutsches Modell
nlp = spacy.load("de_core_news_md")  # md statt sd

# Woerter einlesen
woerter = []
datei = 'Essen_kochen.txt'
with open(datei, 'r') as datei_handle:
    for line in datei_handle.readlines():
        woerter.append(line.strip())
print(woerter)

# Ähnlichkeit zwischen den Wörtern berechnen
similarity = numpy.zeros((len(woerter), len(woerter)))
for idx1, wort1 in enumerate(woerter):
    for idx2, wort2 in enumerate(woerter):
        similarity_1_2 = nlp(wort1).similarity(nlp(wort2))
        similarity[idx1, idx2] = similarity_1_2

# Aus diesen Wörtern suchen wir uns ein zufälliges aus
zufallszahl = random.randint(0, len(woerter))  # eine Zahl zwischen 0 und Länge der Wörter
zufallswort = woerter[zufallszahl]  # so bekommen wir das Zufallswort
print(zufallswort)  # hier auskommentieren nach dem Testen!

geraten = False
runden = 0
n_aehnlich = 5 # das wievielt ähnlichste Wort wir nehmen (nicht 0 (gibts nicht), und nicht 1, das verrät das Wort)

while geraten == False:
    if runden == 0:
        wort = input(f'Ich habe ein zufälliges Wort ausgesucht ({len(zufallswort)} Buchstaben)\nrate das Wort: ')
    else:
        wort = input('rate nochmal: ')
    runden += 1

    if wort == zufallswort:
        print(f'Yeah du hast es geschafft!! Das Wort war {zufallswort}. Das war super!')
        print(f'Du hast {runden} Versuche gebraucht')
        geraten = True
    if runden > 3 and wort !=zufallszahl:
        # hier geben wir einen Tipp
        # dazu suchen wir das n. ähnlichste Wort aus der Sammlung
        aehnliche_woerter = numpy.argsort(similarity[zufallszahl, :])
        aehnliches_wort = (woerter[aehnliche_woerter[-n_aehnlich]])

        if n_aehnlich == 1:
            print(f'Hier ist die Lösung: {zufallswort}')
            geraten = True  # steigt aus der while Schleife aus
        else:
            print(f'Hier ist ein Tipp: {aehnliches_wort} ist ein ähnliches Wort')
        n_aehnlich -= 1
    # nochmal spielen Abfrage einbauen
    # schönerer Hintergrund mit pygame??