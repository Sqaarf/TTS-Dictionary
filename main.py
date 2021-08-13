from tts import TextToSpeech as TTS
from dictio import Dictio

if __name__ == '__main__':
	word = input("Word you want the definition : ")
	defi = " ".join(Dictio().scrape(word))
	print(defi)
	TTS().run(defi)
	
