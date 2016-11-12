import json
import sys

from subprocess import check_output

import tools


with open('output/output.json', 'w') as outfile:
    json.dump(clean_program_data, outfile)
