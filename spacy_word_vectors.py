import spacy
import numpy
from spacy.lang.de.examples import sentences

# wir laden ein deutsches Modell
nlp = spacy.load("de_core_news_sm")

# wir laden eine Datei
datei = 'saetze.txt'
with open(datei, 'r') as datei_handle:
    saetze = datei_handle.readlines()
saetze_ohne_newline = [satz.strip() for satz in saetze]

alle_woerter = []
satz_vektoren_spacy = numpy.zeros((len(saetze), 96))
for idx, satz in enumerate(saetze_ohne_newline):
    # lasst uns den Satz in Wörter zerteilen
    woerter = satz.split(' ')
    print(woerter)
    spacy_satz = nlp(satz)
    satz_vektoren_spacy[idx, :] = spacy_satz.vector
    # nun kommen die neuen Wörter zu alle_woerter dazu
    alle_woerter = alle_woerter + woerter
    # Listen können wir wieder mit + zusammen fügen

# also nächstes möchten wir die Wörter zählen, die wir darin finden
print('so viele Wörter haben wir eingelesen:')
print(len(alle_woerter))


print('so viele verschieden gibt es:')
print(len(set(alle_woerter)))
# das hier ist ein Trick mit set()

# jetzt gehen wir durch jeder Wort und schauen, welches Wort daneben ist
# wörter zu index:
# Jedes Wort bekommt eine Zahl zugewiesen, mit der wir es wieder finden
alle_verschiedenen_woerter = list(set(alle_woerter))
woerter_zu_index = {}
index_zu_woerter = {}
for wort_index, wort in enumerate(alle_verschiedenen_woerter):
    woerter_zu_index[wort] = wort_index
    index_zu_woerter[wort_index] = wort

# jetzt zählen wir
wort_vektoren = numpy.zeros((len(alle_verschiedenen_woerter), len(alle_verschiedenen_woerter)))
for satz in saetze_ohne_newline:
    woerter = satz.split(' ')
    for wort_position, wort in enumerate(woerter):
        wort_index = woerter_zu_index[wort]

        max_position = numpy.min([len(woerter), wort_position + 3 + 1])
        min_position = numpy.max([0, wort_position - 3])
        nachbar_woerter = woerter[min_position:wort_index] + woerter[wort_index+1:max_position]

        for nachbar_wort in nachbar_woerter:
            wort_index_nachbar = woerter_zu_index[nachbar_wort]
            wort_vektoren[wort_index, wort_index_nachbar] += 1


print(wort_vektoren[:,:])

print(satz_vektoren_spacy)




