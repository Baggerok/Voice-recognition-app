import json

def parse_bindings (file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def parse_phrase (phrase):
    return phrase.split()

def toggle_parsing (pharse_parsing):
        phrase_parsing = not phrase_parsing
        print("Changed parsing mode to " + phrase_parsing)