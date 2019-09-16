import re

f = open('sample.txt', 'r')

all_lines = f.readlines()
replacements = {}

expression = r'\{(.*?)\}'

for line in all_lines:
    matches = re.findall(expression, line)
    if matches:
        for match in matches:
            if match not in replacements:
                value = input(f'Tell me a {match}:')
                replacements[match] = value

for line in all_lines:
    print(line.format(**replacements))
