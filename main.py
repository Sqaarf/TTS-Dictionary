from tts import TextToSpeech as TTS
from dictio import Dictio

if __name__ == '__main__':

	defi = " ".join(Dictio().scrape('chair'))
	print(defi)
	TTS().run(defi)
	