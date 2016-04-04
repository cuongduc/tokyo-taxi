from data_parser import read_data
import json

raw_string = read_data()

print(json.dumps(raw_string))