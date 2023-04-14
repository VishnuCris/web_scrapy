
from bs4 import BeautifulSoup

class BeautifulSoapService:
	def __init__(self):
		pass

	def paragraph_scrap_fun(self,content,parser="html.parser"):
		soup = BeautifulSoup(content,parser)
		return soup