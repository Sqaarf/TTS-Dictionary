import requests
from bs4 import BeautifulSoup

class Dictio():
	def __init__(self):
		self.url = "https://www.dictionary.com/browse/"

	def scrape(self, word):
		self.url += word

		page = requests.get(self.url)
		soup = BeautifulSoup(page.content, 'html.parser')
		raw = soup.select(".e1q3nk1v3")
		clean = [x.text for x in raw]
		return clean[0:3]
		

'''
def_list = Dictio().scrape("test")
for i in def_list:
	print(i)
	print()
'''