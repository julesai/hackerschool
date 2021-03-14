import spacy
import numpy


# wir laden ein deutsches Modell
nlp = spacy.load("de_core_news_md")  # md statt sd

# wir laden eine Datei
datei = 'saetze.txt'
with open(datei, 'r') as datei_handle:
    saetze = datei_handle.readlines()
saetze_ohne_newline = [satz.strip() for satz in saetze]

# similarity
similarity = numpy.zeros((len(saetze), len(saetze)))
for idx1, satz1 in enumerate(saetze):
    for idx2, satz2 in enumerate(saetze):
        similarity_1_2 = nlp(satz1).similarity(nlp(satz2))
        similarity[idx1, idx2] = similarity_1_2

print(similarity)

# wir schauen mal für speziellen Satz an
# suche hier den Satz heraus
index_s = 32
print('Satz:')
print(saetze[index_s])
aehnliche_saetze = numpy.argsort(similarity[index_s, :])
print('Die Ergebnisse:')
for idx in range(2, 5):
    # top 3 Ergebnisse
    # wir wollen die 0 nicht,
    # wir wollen die -1 nicht, da sie der Original Satz sein wird
    print(saetze_ohne_newline[aehnliche_saetze[-idx]])  # pass auf das Minus auf :-)