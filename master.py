from flask import Flask, request
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return {"message": "home page"}

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if city.isdigit():
        res = "City name must be string e.g. 'Amsterdam, Berlin'"
        return res
    response = requests.get("http://weather:3002/weather?city="+ city)
    return response.json()
                                                              
@app.route('/news')
def news():
    country_name = request.args.get('country')
    if country_name.isdigit() or len(country_name) > 2 :
        resp = "Country name must be string. Choose from: ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za"
        return resp
    response = requests.get("http://news:3003/news?country="+ country_name)
    return response.json()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3001,debug=True,threaded=True)
