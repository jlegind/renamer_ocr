'''Module to extract the grammar from a sentence so that each word is spacy analyzed for its grammatical label.'''
import spacy

from spacy.cli import download


spacInfo = spacy.info(markdown=True) # For checking if 'en_core_web_sm' is loaded
spinfo = spacInfo.split()
print('!#!#!#!', spinfo, type(spinfo))
if 'en_core_web_sm' not in spinfo: # Performs the above check
    print("Downloading -en_core_web_sm-")
    download("en_core_web_sm")
else:
    print("\n'en_core_web_sm' is already loaded :D")


# load english language model
nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])
# Creates the language analyzer.

# nlp.tokenizer.rules = {key: value for key, value in nlp.tokenizer.rules.items() if "'" not in key and "’" not in key and "‘" not in key}
# print("Asserting ' rule")
# print('asseryion==', [t.text for t in nlp("can't")] == ["can't"])
# print("End assertion---")
#
# text = text.replace("'", '')
### DID NOT work for the rule of ignoring the can't with apostrophe.

text = "Don't FORGET TO Cat YOUR LuncH And Make SoMe TRouBLE"
# create spacied text
doc = nlp(text)
grams = []  # List that will contain the gammar for each word
for token in doc:
    grams.append(token.pos_) # pos_ is the grammar labels: https://spacy.io/usage/linguistic-features

# text.replace("'", '') # Taking out all apostrophes
text = text.split() # We need the text as a list

for ps, val in enumerate(grams): # By enumerating we get a position and a grammar value for each word in the text.
    if ps+1 <= len(grams):

        gram_test = val , grams[ps+1]
        if gram_test == ('PROPN', 'PRON'): # If proper Noun is followed by a pronoun then we display a warning.
            print(f"We might have a problem with {gram_test} near #{text[ps]}# @ position {ps} in {text}")
            break
    else:
        print("List exhausted!")