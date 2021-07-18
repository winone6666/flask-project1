from flask import Flask, render_template
from data import tours as tour, departures as depart, subtitle, description, title

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title=title, tours=tour, subtitle=subtitle, departures=depart,
                           description=description)


@app.route('/departures/<string:departure>')
def departures(departure):
    lst_depart = []
    price_depart = []
    count_nights = []

    for t in tour:
        if departure == tour[t]['departure']:
            lst_depart.append(t)
            price_depart.append(tour[t]['price'])
            count_nights.append(tour[t]['nights'])
    return render_template('departure.html', title=title, tours=tour, subtitle=subtitle,
                           lst_departures=lst_depart, departures=depart, city=departure,
                           description=description, price_depart=price_depart, count_nights=count_nights)


@app.route('/tours/<int:id>/')
def tours(id):
    return render_template('tour.html', title=title, tour_title=tour[id]['title'],
                           country=tour[id]['country'], departure=depart[tour[id]['departure']], departures=depart,
                           nights=tour[id]['nights'], description=tour[id]['description'],
                           picture=tour[id]['picture'], price=tour[id]['price'], stars=tour[id]['stars'])
app.run()