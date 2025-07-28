import sounddevice as sd
from vosk import Model, KaldiRecognizer
import queue
import sys
import json
import os

import input

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def main():
    MODEL_PATH = os.path.join("Models", "vosk-model-small-ru-0.22")
    model = Model(MODEL_PATH)

    device_info = sd.query_devices(None, "input")
    samplerate = int(device_info["default_samplerate"])
    try:
        with sd.RawInputStream(
                samplerate=samplerate,
                blocksize=8000,
                dtype="int16",
                channels=1,
                callback=callback):
            
            rec = KaldiRecognizer(model, samplerate)
            rec.SetWords(True)

            Moder = input.Mode_handler()

            while True:
                data = q.get()

                # recognized
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    phrase = result.get("text", "")
                    
                    Moder.mode_recognition(phrase)
                    Moder.mode_exec(phrase)

                """partial
                else:
                    partial = json.loads(rec.PartialResult())
                    print(partial.get("partial", ""))
                """
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Error occured: {e}")
        
if __name__ == "__main__":
    main()
