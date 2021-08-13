import pyttsx3

class TextToSpeech():
	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('rate', 125)
	
	def run(self, text):
		self.engine.say(text)
		self.engine.runAndWait()
		self.engine.stop()
