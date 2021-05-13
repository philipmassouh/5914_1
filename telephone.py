import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("-LsDW7oVqIm2_wjDZeAcEnt5c3kmjqKoP7DWl90PX4BV")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/2f7e501b-7dfb-4fc8-90e0-753de2e3af0e')


sentence = input("Player 1, enter sentence: ")

languages = ['en-es', 'es-fr', 'fr-en']
translated_sentence = sentence

for language in languages:
    translation = language_translator.translate(
        text=translated_sentence,
        model_id=language).get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    translated_sentence = translation['translations'][0]['translation']

print(translated_sentence)
