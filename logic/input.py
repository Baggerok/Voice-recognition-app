from pynput.keyboard import Key, Controller
from logic import parser as parse
import time

keyboard = Controller()
parser = parse.Parser()

class Mode_handler:
    def __init__(self):
        self.__modes = ["отключить", "игровой режим", "печать голосом"]
        self.__utilities = ["режим фраз"]
        self.__funcs = [self.mode_default, self.mode_gaming, self.mode_typing, parser.toggle_sentence_parsing]
        self.__current_mode = 0
        self.mode_changed = False

    def mode_recognition(self, phrase):
        if phrase in self.__modes:
            self.__current_mode = self.__modes.index(phrase)
            self.mode_changed = True
            print("Changed mode to " + self.__modes[self.__current_mode])
        else:
            self.mode_changed = False

    def util_recognition(self, phrase):
        if phrase in self.__utilities:
            index = self.__utilities.index(phrase)
            self.__funcs[len(self.__modes) + index](phrase)

    def mode_exec(self, phrase):
        if not self.mode_changed:
            self.__funcs[self.__current_mode](phrase)

    def press_key(self, key):
        keyboard.press(key)
        time.sleep(0.01)
        keyboard.release(key)

    def mode_typing(self, phrase):
        self.print("Typing...")
        for key in phrase:
            self.press_key(key)

    def mode_gaming(self, phrase):
        if parser.phrase_parsing:
            parsed_phrase = parser.parse_phrase(phrase)
            word_found = False
            for word in parsed_phrase:
                key = parser.binds.get(word)
                if key:
                    print("pressing " + key)
                    self.press_key(key)
                    word_found = True
            if not word_found:
                print("gaming...")
        else:
            key = parser.binds.get(phrase)
            if key:
                print("pressing " + key)
                self.press_key(key)
            else:
                print("gaming...")

    def mode_default(self, phrase):
        if phrase != "":
            print(phrase)