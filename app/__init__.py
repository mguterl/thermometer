import temperature

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/temperature")
def temperature():
  sensor = temperature.sensor('/dev/ttyACM0')
  return jsonify(sensor.current_temperature().__dict__)

