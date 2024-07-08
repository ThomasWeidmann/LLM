import os
import json



input_file_path = 'D:\Informatik\llm\c4-train.00000-of-01024.json'
output_file_path = 'D:\Informatik\llm\c4-train.00000-of-01024_cleaned.json'

allowed_characters = {chr(i) for i in range(32, 127)}

def is_line_allowed(line):
    return all(c in allowed_characters for c in line)

with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if is_line_allowed(line.rstrip('\n')):
            d = json.loads(line)
            outfile.write(d["text"])


