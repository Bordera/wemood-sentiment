import json
import sys

from subprocess import check_output
from datetime import datetime as dt
from pymongo import MongoClient

import tools
import record
import transcribe
import sentiment

client = MongoClient()
db = client.wemood

# record audio

output_data = {"date":unicode(dt.now())}
file_name = tools.randwavefile()
record_file = record.record_audio(sys.argv[1], file_name)

## extract text
# https://cloud.google.com/speech/docs/languages

sound_output = transcribe.transcribe(record_file,sys.argv[2])
output_data["transcription_data"]= sound_output
sentiment_output = sentiment.get_text_sentiment(sound_output["results"][0]["alternatives"][0]["transcript"])
output_data["sentiment_data"] = sentiment_output
output_data["sentiment_score"] = sentiment_output['docSentiment']['score']

output_data["sensor"]= "sentiment"

# write_output
with open('output/output.json', 'w') as outfile:
    json.dump(output_data, outfile)

db.sensors.insert_one(output_data)
