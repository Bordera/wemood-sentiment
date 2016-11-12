import json

from time import sleep
from subprocess import Popen

with open('config.json') as data_file:
    config = json.load(data_file)

refresh_rate = config["refresh_rate"]
capture_rate = config["capture_rate"]

while True:
    Popen(["python","sensor.py",capture_rate])
    sleep(float(refresh_rate))
