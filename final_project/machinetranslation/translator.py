"""
Language translator using IBM Watson Language Translation API
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """English to French translation"""
    if english_text is not None:
        translation_response = language_translator.translate(text=english_text, model_id='en-fr')
        french_text = translation_response.get_result()
        translation = french_text['translations'][0]['translation']
    else:
        translation = ''

    return translation


def french_to_english(french_text):
    """French to English translation"""
    if french_text is not None:
        translation_response = language_translator.translate(text=french_text, model_id='fr-en')
        english_text = translation_response.get_result()
        translation = english_text['translations'][0]['translation']
    else:
        translation = ''

    return translation
