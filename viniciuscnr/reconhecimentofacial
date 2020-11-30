import speech_recognition as sr 
import pyaudio

def reconhece():
        rec= sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google (audio, language="pt")
                    return "Voce disse: {}".format(entrada)
                except sr.UnknownValueError:
                    return "Nao entendi"
print("Ouvindo...")
while True:
    fala=reconhece()
    print(fala)
