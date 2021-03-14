import spacy

# python -m spacy download de_core_news_sm
# https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.0.0/de_core_news_sm-3.0.0-py3-none-any.whl

from spacy.lang.de.examples import sentences

nlp = spacy.load("de_core_news_sm")
#doc = nlp(sentences[0])

doc = nlp('Das ist mein Testsatz, den ich gerne bearbeiten würde.')
doc = nlp('was ist eine Ente, ist das ein kleines Tier oder ein großes Tiergit')

print(doc.text)

anzahl_nomen = 0

for token in doc:
    print(token.text, token.pos_)
    if token.pos_ == 'NOUN':
        anzahl_nomen = anzahl_nomen + 1

print(f'so viele Nomen: {anzahl_nomen}')
