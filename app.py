from flask import Flask, render_template, request
from cs50 import SQL
import random
import datetime
import json
import requests
import pycountry
import re

app = Flask(__name__)
db = SQL("sqlite:///search.db")

def convert(country_code):
    country = pycountry.countries.get(alpha_2=country_code)
    return country.name

def getCity():
    try:
        with open("assets/country-list.json", "r") as file:
            cities = json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return render_template("apology.html")
    except json.JSONDecodeError:
        print("File is not in valid JSON format!")
        return render_template("apology.html")

    try:
        city = random.choice(cities)["capital"]
    except (IndexError, TypeError, KeyError):
        print("File does not contain expected data!")
        return render_template("apology.html")

    return city

def sanitize_city(city):
    if not isinstance(city, str):
        return None
    city = re.sub(r'\W+', '', city) # Remove non-alphanumeric characters
    city = city.strip().lower() # Remove extra spaces and convert to lowercase
    return city

def update_db(city_searched):
    rows = db.execute("SELECT * FROM search WHERE city_name = ?", city_searched)
    if len(rows) != 0:
        db.execute("UPDATE search SET count = count + 1 WHERE city_name = ?", city_searched)
    else:
        db.execute("INSERT INTO search(city_name) VALUES(?)", city_searched)

def search(city, units, API_KEY="64f60853740a1ee3ba20d0fb595c97d5"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    response = requests.get(url).json()

    if response["cod"] == 200:
        if request.method == "POST" and response["cod"] == 200:
            city_searched = sanitize_city(request.form.get("city")).title()
            if city_searched is None:
                return render_template("apology.html")
            else:
                update_db(city_searched)
        country = convert(response["sys"]["country"])
        date = datetime.date.today().strftime("%B %d, %Y")
        forecast = response["weather"][0]["main"]
        temperature = round(response["main"]["temp"])
        min = round(response["main"]["temp_min"])
        max = round(response["main"]["temp_max"])
        feel = round(response["main"]["feels_like"])
        humidity = response["main"]["humidity"]
        wind = response["wind"]["speed"]
        pressure = response["main"]["pressure"]
        rows = db.execute("SELECT * FROM search ORDER BY count DESC LIMIT 3")

        print(rows)

        return render_template("index.html", city=city, country=country, date=date, forecast=forecast, temperature=temperature, min=min, max=max, feel=feel, humidity=humidity, wind=wind, pressure=pressure, rows=rows)
    else:
        return render_template("apology.html")

@app.route("/", methods=["GET", "POST"])
def index():
    unit = "metric"
    if request.args.get("unit") == "C":
        unit = "metric"
    elif request.args.get("unit") == "F":
        unit = "imperial"


    if request.method == "POST":
        city = request.form.get("city")
        return search(city.title(), units=unit)
    else:
        city = getCity()
        return search(city.title(), units=unit)