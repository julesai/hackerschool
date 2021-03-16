import spacy
import numpy
import random
# hier lassen wir die Spieler ein Wort raten und geben bei jedem Versuch an, wie nah sie sind
# Idee: auch als Farbe angeben (rot..blau, heiß und kalt)

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
    else:
        aehnlichkeit = nlp(wort).similarity(nlp(zufallswort))
        print(f'Dein Wort ist so ähnlich: (Zahl zwischen 0 und 1): {round(aehnlichkeit, 2)}')
    # Idee: noch einen Tipp einbauen

    # nochmal spielen Abfrage einbauen
    # schönerer Hintergrund mit pygame??
    # Abbruchabfrage mit keyboard interrupt