import spacy
from spacy.cli import download
from spacy.tokenizer import Tokenizer


spacInfo = spacy.info(markdown=True)
spinfo = spacInfo.split()
print('!#!#!#!', spinfo, type(spinfo))
if 'en_core_web_sm' not in spinfo:
    print("DOwnloading -en_core_web_sm-")
    download("en_core_web_sm")
sent="Don't FORGET TO Cat YOUR LuncH And Make SoMe TRouBLE"
nlp=spacy.load('en_core_web_sm')
nlp.tokenizer = Tokenizer(nlp.vocab)
doc=nlp(sent)
grams = []
for token in doc:
    print(token.text, token.pos_)
    grams.append(token.pos_)
print("Final list::", grams)
LSent = sent.split()
for ps, val in enumerate(grams):
    if ps+1 <= len(grams):
        print(f"ps:{ps} -- val:{val}")
        print(LSent[ps])
        print(val , grams[ps+1])
        gram_test = val , grams[ps+1]
        print(f"Gram test = {gram_test}")
        if gram_test == ('PROPN', 'PRON'):
            print(f"We might have a problem with {gram_test} near {LSent[ps]} @ position {ps}")
            break
    else:
        print("List exhausted!")