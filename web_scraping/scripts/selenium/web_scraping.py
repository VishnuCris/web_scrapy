# from web_scraping.services.SeliniumService import SeliniumServiceCls
from selenium import webdriver



def extract_site():
	elements = {'url':'https://www.w3schools.com'}
	# SeliniumInstance = SeliniumServiceCls(elements)
	contents = open_driver(elements)
	return contents

def open_driver(elements):
		chrome_driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
		chrome_driver.get(elements.get('url'))
		content = chrome_driver.page_source
		return content