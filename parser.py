import json

def parse_bindings (file):
    with open(file, "r", encoding="utf-8") as f:
        parsed = json.load(f)
    return parsed