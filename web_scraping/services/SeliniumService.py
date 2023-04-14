from selenium import webdriver

class SeliniumServiceCls:
	def __init__(self,ele={}):
		self.url = ele.get('url')
		self.chrome_driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

	def open_driver(self):
		chrome_driver.get(self.url)
		content = chrome_driver.page_source
		return content

