import sounddevice as sd
from vosk import Model, KaldiRecognizer

import threading
import queue
import sys
import json
import os

import config


MODEL_PATH = config.from_root("resources", "Models", "vosk-model-small-ru-0.22")

class Recognizer:
    def __init__(self):
        self.stop_recognition = False
        self.que = queue.Queue()
        self.model = Model(MODEL_PATH)
        self.device_info = sd.query_devices(None, "input")
        self.samplerate = int(self.device_info["default_samplerate"])

    def callback(self, indata, frames, time, status):
        self.que.put(bytes(indata))

    def recog_loop(self,Moder):
        with sd.RawInputStream(
                samplerate = self.samplerate,
                blocksize = 8000,
                dtype = "int16",
                channels = 1,
                callback = self.callback):
            
            rec = KaldiRecognizer(self.model, self.samplerate)
            rec.SetWords(True)

            while self.stop_recognition == False:
                data = self.que.get()

                # recognized
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    phrase = result.get("text", "")
                    
                    Moder.mode_recognition(phrase)
                    Moder.util_recognition(phrase)
                    Moder.mode_exec(phrase)