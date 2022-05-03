"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""

import re

with open("text.txt") as text:
    data = text.readlines()
    
pattern = re.compile('([A-Z][\w]+)([ \w ]*)([A-Z][\w]+)')

for person in data:
    match = pattern.search(person)
    
    if match:
        print(f'{match.group(3)}')
    else:
        print(None)