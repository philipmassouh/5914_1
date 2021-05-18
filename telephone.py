import json
import time

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('-LsDW7oVqIm2_wjDZeAcEnt5c3kmjqKoP7DWl90PX4BV')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

# Input should be some complex sentence in case it will have some real changes, for example: how are you.
sentence = input("Player 1, enter sentence: ")

# english, italian, german, french, english
languages = ["en-it", "it-de", "de-fr", "fr-en"]

for i in range(4):
    translation = language_translator.translate(
        text=sentence,
        model_id=languages[i]).get_result()
    result = json.dumps(translation, indent=2, ensure_ascii=False)
    sentence = translation.get('translations')[0]['translation']
    print("Player" + str(i+2) + ", languages: " + languages[i])
    print(sentence)
    time.sleep(1)
