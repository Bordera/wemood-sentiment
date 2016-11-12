import json

from time import sleep
from subprocess import Popen

import record

with open('config.json') as data_file:
    config = json.load(data_file)

refresh_rate = config["refresh_rate"]
capture_rate = config["capture_rate"]
language = config["language"]

# http://g.co/cloud/speech/docs/languages



while True:
    Popen(["python","sensor.py",capture_rate, language])
    sleep(float(refresh_rate))
