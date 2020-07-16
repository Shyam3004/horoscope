import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def first():
    return render_template('first.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    serviceurl = 'http://horoscope-api.herokuapp.com/horoscope/today/'
    name = request.form['name']
    sunsign = request.form['sunsign']
    url = serviceurl + sunsign
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    # print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    # print(json.dumps(info, indent=4))
    horoscope = info['horoscope']
    date_today = info['date']
    # print('your today horoscope : \n    ' + horoscope)
    return render_template('result.html', name=name, sunsign=sunsign, date_today=date_today, horoscope=horoscope)

if __name__ == "__main__":
    app.run()
