from pynput.keyboard import Key, Controller
import parser
import time

keyboard = Controller()

binds = parser.parse_bindings("bindings.json")

class Mode_handler:
    def __init__(self):
        self.__modes = ["отключить", "игровой режим", "печать голосом"]
        self.__funcs = [mode_default, mode_gaming, mode_typing]
        self.__current_mode = 0
        self.mode_changed = False

    def mode_recognition(self, phrase):
        if phrase in self.__modes:
            self.__current_mode = self.__modes.index(phrase)
            self.mode_changed = True
            print("Changed mode to " + self.__modes[self.__current_mode])
        else:
            self.mode_changed = False

    def mode_exec(self, phrase):
        if self.mode_changed != True:
            self.__funcs[self.__current_mode](phrase)

def mode_typing (phrase):
    print("Typing...")
    for letter in phrase :
        keyboard.press(letter)
        time.sleep(0.01)
        keyboard.release(letter)

def mode_default(phrase):
    if phrase != "":
        print(phrase)

def mode_gaming (phrase):
    key = binds.get(phrase)
    if key:
        print("pressing " + key)
        keyboard.press(key)
        time.sleep(0.01)
        keyboard.release(key)
    else:
        print("gaming...")