import json
import sys

from subprocess import check_output

import tools
import record
import transcribe

# record audio

#file_name = tools.randwavefile()
#record.record_audio(sys.argv[1], file_name)

# extract text https://cloud.google.com/speech/docs/languages

file_name = "data/PMYVU.wav"
sound_text = transcribe.transcribe(file_name,sys.argv[2])
print(sound_text)

# extract sentiment






#with open('output/output.json', 'w') as outfile:
#    json.dump(sentiment_output, outfile)
