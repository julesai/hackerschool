# Hier ist ein Beispiel um Sätze aus einer Textdatei einzulesen

# so heisst die Datei
datei = 'saetze.txt'

# Wir benutzen ein lustiges Konstrukt mit with um die Datei auch wieder automatisch zu schließen
# dann müssen wir nicht daran denken, falls etwas beim verarbeiten schief geht
with open(datei, 'r') as datei_handle:
    saetze = datei_handle.readlines()
    # hier bekommen wir nun eine Liste von Sätzen (da sie in unserer Datei als verschiedene Zeilen eingetragen sind)

# so sieht es aus
print(saetze)

# sind dir die '\n' am Ende jedes Satzes aufgefallen?
# so werden wir sie los
# erstmal eine leere Liste
saetze_ohne_newline = []
for satz in saetze:
    # hier lassen wir das \n am Ende weg
    satz = satz.strip()
    # hier wird ein neues Element in eine leere Liste eingefügt
    saetze_ohne_newline.append(satz)

print(saetze_ohne_newline)

# oder für die Fortgeschrittenen:
saetze_ohne_newline_2 = [satz.strip() for satz in saetze]
print(saetze_ohne_newline_2)

# so, nun lass uns mal den dritten Satz anschauen
print('der dritte Satz:')
print(saetze_ohne_newline[2])
# dir ist wahrscheinlich aufgefallen, dass wir hier eine 2 geschrieben haben und keine 3
# python fängt bei 0 an zu zählen
# und schaue, wir haben hier eckige Klammern benutzt um ein bestimmtes Element zu bekommen

print('der erste Satz:')
print(saetze_ohne_newline[0])

# und jetzt der letzte Satz
print('der letzte Satz')
print(saetze_ohne_newline[-1])
# das geht mit -1
