from flask import Flask
from web_scraping.routes.route import web_scrap

app = Flask(__name__)

app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'


app.register_blueprint(web_scrap)