import random
# so importieren wir verschiedene Pakete
# import paketname

# danach können wir sie benutzen
# random kann uns eine Zufallszahlen generieren
# man benutz es mit paketname.funktionsname
zufallszahl = random.random()

print(zufallszahl)

# hier schauen wir sie uns mal an mit einer Schleife
print('Hier kommen viele Zufallszahlen:')
for idx in range(10):
    zufallszahl = random.random()
    print(zufallszahl)

# hier suchen wir eine zufällige ganze Zahl von 0 bis 9
print('Hier kommen ganze Zufallszahlen')
for idx in range(10):
    zufallszahl = random.randint(0, 9)
    print(zufallszahl)

# ändere den Code, so dass die Zufallszahlen von 1 bis 20 gehen

# wenn ihr mehr über ein bestimmtes Paket wissen wollt, dann googelt ihr es am besten

