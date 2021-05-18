import json
import time
from difflib import SequenceMatcher
import sys
import string

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if len(sys.argv) != 2 or (sys.argv[1] != "demo" and sys.argv[1] != "play"):
    sys.exit("Improper command line argument. Expected 'telephone.py [demo/play]'")

authenticator = IAMAuthenticator('-LsDW7oVqIm2_wjDZeAcEnt5c3kmjqKoP7DWl90PX4BV')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

# Input should be some complex sentence in case it will have some real changes, for example: how are you.
sentence = input("Player 1, enter sentence: ")
answer = sentence

# english, italian, german, french, english
languages = ["en-it", "it-de", "de-fr", "fr-en"]
separator = "-"*15

for i in range(4):
    translation = language_translator.translate(
        text=sentence,
        model_id=languages[i]).get_result()
    result = json.dumps(translation, indent=2, ensure_ascii=False)
    sentence = translation.get('translations')[0]['translation']
    print(f"Translated from {languages[i][:2]} to {languages[i][3:]}")
    if sys.argv[1] == "demo" and i < 3:
        print(separator)
        print(f"Sentence: {sentence}")
    time.sleep(1)
print(separator)

print(f"\n{separator}")
print(f"The sentence is: {sentence}")
print(f"{separator} \n")
guess = input("Player 2, make your guess: ")
print(f"Similarity score: {str(similar(answer.lower(), sentence.lower())*100)[:4]}%")
