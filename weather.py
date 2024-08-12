from flask import Flask, render_template, request
import requests
from config import WHEATHER_API_KEY

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        #weather = get_weather(city)
        #news = get_news()
    return render_template("index.html", weather=weather)

def get_weather(city):
    if city:
        city

    api_key = WHEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    return response.json()


