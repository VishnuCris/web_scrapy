from flask import jsonify
import requests
from web_scraping.services.BeautifulSoapService import BeautifulSoapService
from web_scraping.services.SeliniumService import SeliniumServiceCls


class BaseView(object):
	def __init__(self):
		self.BeautifulSoup = BeautifulSoapService()

	def BaseWebScraping(self,url,element_details):
		response = requests.get(url)
		content = response.content
		soup = self.BeautifulSoup.paragraph_scrap_fun(content,"html.parser")

		### Extracting apporopirate elements details given as input ###
		result_dict = {}
		for ele_obj in element_details:
			element = soup.findAll(ele_obj.get('element'),attrs={ele_obj.get('attribute'):ele_obj.get('attribute_value')})
			result_dict[ele_obj.get('detail_name')] = []
			for ele in element:
				strr = str(ele.text)
				### replacing unicodes in dtring ###
				strr = strr.encode("ascii","ignore")
				strr = strr.decode()
				###  end ###
				result_dict[ele_obj.get('detail_name')].append(strr)

		return result_dict

		

