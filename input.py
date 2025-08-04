from pynput.keyboard import Key, Controller
import parser as parse
import time

keyboard = Controller()

parser = parse.Parser()

class Mode_handler:
    def __init__(self):
        self.__modes = ["отключить", "игровой режим", "печать голосом"]
        self.__utilities = ["изменить чтения"]
        self.__funcs = [mode_default, mode_gaming, mode_typing, parser.toggle_parsing]
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
        if self.mode_changed != True:
            self.__funcs[self.__current_mode](phrase)
                
def press_key (key):
    keyboard.press(key)
    time.sleep(0.01)
    keyboard.release(key)

def mode_typing (phrase):
    print("Typing...")
    for key in phrase :
        press_key(key)

def mode_gaming (phrase):
    if parser.phrase_parsing:
        parsed_phrase = parser.parse_phrase(phrase)
        word_found = False
        for word in parsed_phrase:
            key = parser.binds.get(word)  

            if key:
                print("pressing " + key)
                press_key(key)
                word_found = True
        if not word_found:
            print("gaming...")
    else:
        key = parser.binds.get(phrase)
      
        if key:
            print("pressing " + key)
            press_key(key)
        else:
            print("gaming...")

def mode_default(phrase):
    if phrase != "":
        print(phrase)

