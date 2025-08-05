import json
import config

BINDINGS_PATH =  config.from_root("resources", "bindings.json")

class Parser:
    def __init__(self):
        self.binds = self.__parse_bindings(BINDINGS_PATH)
        self.phrase_parsing = False

    def __parse_bindings (self, file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def parse_phrase (self, phrase):
        return phrase.split()

    def toggle_parsing (self, phrase):
            self.phrase_parsing = not self.phrase_parsing
            print("Changed parsing mode to " + str(self.phrase_parsing))