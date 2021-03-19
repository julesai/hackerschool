# Ein kleines Spiel bei dem man Woerter raten kann
import random

# Woerter einlesen
woerter = []
datei = 'Essen_kochen.txt'
with open(datei, 'r') as datei_handle:
    for line in datei_handle.readlines():
        woerter.append(line.strip())
print(woerter)

# Aus diesen Wörtern suchen wir uns ein zufälliges aus
zufallszahl = random.randint(0, len(woerter))# eine Zahl zwischen 0 und Länge der Wörter
zufallswort = woerter[zufallszahl]  # so bekommen wir das Zufallswort
print(zufallswort)     # hier auskommentieren nach dem Testen!


geraten = False
runden = 0

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





