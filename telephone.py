from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('-LsDW7oVqIm2_wjDZeAcEnt5c3kmjqKoP7DWl90PX4BV')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')


sentence = input("Player 1, enter sentence: ")
