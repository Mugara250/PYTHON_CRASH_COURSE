#!/usr/bin/python3
from pathlib import Path
import json


path = Path('favorite_number.json')
if path.exists():
    path = Path('favorite_number.json')
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {contents}.")
else:
    favorite_number = int(input("What is your favorite number? "))
    contents = json.dumps(favorite_number)
    path.write_text(contents)


