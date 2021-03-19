# Hier sehen wir, wie man eine Schleife baut

# range macht uns eine Folge von Zahlen
for index in range(10):
    # ab hier wird um 4 Leerzeichen eingerückt, so lange bis die Schleife vorbei ist
    print(index)
    # hier kommt alles, was die Schleife tun soll
print('Jetzt sind wir fertig')

# Bis zu welcher Zahl zählt die Schleife?
# Bei welcher Zahl geht es los?
# Hast du den Doppelpunkt gesehen?


# Jetzt schreibe du eine Schleife, die von 0 bis 19 zählt
######
######

Alter = 12
print('Mein Alter ist: ' + str(Alter))
# if Schleife
# Eine if Schleife fragt eine Bedingung ab, und falls diese erfüllt ist, führt sie den Code danach aus
# der : am Ende ist wichtig
if Alter > 15:
    # ab hier wird um 4 Leerzeichen einerückt, so lange bis der Code innen zu Ende ist
    print('Ich bin älter als 15.')
else:
    # man kann auch Code ausführen, wenn diese Bedingung nicht erfüllt ist
    print('Ich bin jünger als 15.')

# Ändere jetzt das Alter auf 16 und sieh was passiert


# es gibt noch eine weitere Art von Schleifen:
# while macht etwas so lange, bis die Bedingung nicht mehr erfüllt ist
# das heisst man weiß vorher manchmal gar nicht, wie oft die Schleife abläuft
# hier müssen wir zuerst etwas wahres definieren:
# wahr = True
mach_weiter = True
while mach_weiter == True:
    # wir vergleichen den Wert mit einem doppelten ==
    # wir könnten auch vereinfacht sagen
    # while mach_weiter:
    print('Dieser Text kommt, bis du EXIT auf der Konsole eintippst')
    eingabe = input('Tippe hier:')
    if eingabe == 'EXIT':
        mach_weiter = False  # hier setzen wir mach_weiter auf False (nur ein = zum setzen)


# sind dir die Einrückungen aufgefallen?
# du kannst da mal was ändern und sehen, dass der Code nicht mehr laufen wird
