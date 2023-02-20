from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d-%m-%Y')
        url = f"https://api.coingecko.com/api/v3/coins/cardano/history?date={date}"
        response = requests.get(url)
        data = response.json()
        if 'market_data' in data:
            volume = data['market_data']['total_volume']['usd']
            ADAVolume = round(((volume / 2.45) / 1000000), 2)
            return render_template('index.html', date=date, ADAVolume=ADAVolume)
        else:
            return f"No volume data available for Cardano on {date}"
    else:
        return render_template('index.html')
