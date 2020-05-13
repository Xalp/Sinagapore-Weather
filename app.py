from flask import Flask, render_template, redirect, url_for
from weather import get_weather
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    a = get_weather()
    wstr = a[1]
    temp = a[0]
    return "<h2> Today's weather is {}, and the temperature is {}.</h2>".format(wstr, temp)

if __name__ == '__main__':
    app.run(debug=True)