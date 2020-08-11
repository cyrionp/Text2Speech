from gtts import gTTS
from playsound import playsound

while True:
    language=int(input("1) English 2)Turkish\nSelect: "))
    if language==1:
        givenSpeech=input("Say: ")
        tts = gTTS(f"{givenSpeech}",lang="en")
        break
    elif language==2:
        givenSpeech=input("Söyle: ")
        tts = gTTS(f"{givenSpeech}",lang="tr")
        break
    else: print("Select 1 or 2")
tts.save('speech.mp3')
playsound('speech.mp3', True)
