from flask import Blueprint,jsonify,render_template
from web_scraping.views.web_scraping_base import BaseView

web_scrap = Blueprint('web_scrap',__name__,template_folder='templates',static_folder='static')

@web_scrap.get('/')
def scraping_using_selinium():
	return render_template('index.html')


@web_scrap.get('/scrap_product_details')
def paragraph_scrap():
	try:
		base_view_instance = BaseView()

		url = "https://www.flipkart.com/lenovo-ryzen-5-hexa-core-5500u-8-gb-512-gb-ssd-windows-11-home-thinkbook-15-g3-thin-light-laptop/p/itm4e8b7b1c1d272?pid=COMGHEGH5GTHFZRU&lid=LSTCOMGHEGH5GTHFZRUPWHCIS&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=en_H65dyqbBd109v1saq5Wu1VlIFlt2RG0xKWdKgfdqRXngmC4MmnXoJ49%2B7SxtAr3fZHqZTvCSZUUTdIQfETfxZQ%3D%3D&ppt=hp&ppn=homepage&ssid=nvk2my4jpc0000001681475933351&qH=312f91285e048e09"
		element_details = [
			{'element':'span','attribute':'class','attribute_value':'B_NuCI','detail_name':'title'},
			{'element':'div','attribute':'class','attribute_value':'_30jeq3 _16Jk6d','detail_name':'price_details'},
			{'element':'span','attribute':'class','attribute_value':'_3j4Zjq row','detail_name':'Available offers'}
		]

		res = base_view_instance.BaseWebScraping(url,element_details)
		status = True
	except Exception as Err:
		res = str(Err)
		status = False
	return jsonify({'status':status,'response':res})
