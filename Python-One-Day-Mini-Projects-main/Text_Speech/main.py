#text to speech converter

import gtts
import playsound

text = input("Enter something here: ")
sound = gtts.gTTS(text, lang="en")

sound.save('Done.mp3')
playsound.playsound('Done.mp3')
