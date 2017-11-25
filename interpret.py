import requests

luis_url = "https://westcentralus.api.cognitive.microsoft.com/luis/v2.0/apps/2e5b8dc8-3246-4545-ba6d-5c27b5672ac5?subscription-key=3241702170334501bed71110111957e1&spellCheck=true&timezoneOffset=0&q="

def process(utterance):
  interpretation = requests.get(luis_url + utterance).json()
  return interpretation
