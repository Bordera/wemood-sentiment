import json
import sys

from subprocess import check_output
from datetime import datetime as dt

import tools
import record
import transcribe
import interpret

# record audio

output_data = {"date":unicode(dt.now())}
file_name = tools.randwavefile()
record_file = record.record_audio(sys.argv[1], file_name)

## extract text
# https://cloud.google.com/speech/docs/languages

sound_output = transcribe.transcribe(record_file,sys.argv[2])
output_data["transcription_data"]= sound_output
transcription = sound_output["results"][0]["alternatives"][0]["transcript"]
output_data["interpretation"] = interpret.process(transcription)
print(output_data)