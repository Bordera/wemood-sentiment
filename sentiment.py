from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage
import os

def get_text_sentiment(text):
    alchemy_api_key = os.environ["alchemy_api_key"]
    alchemy_language = AlchemyLanguage(api_key=alchemy_api_key)
    result = alchemy_language.sentiment(text=text)
    return result
