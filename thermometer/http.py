from flask import Flask, jsonify

http = Flask(__name__)

@http.route('/')
def index():
  app = http.config['APP']
  current_temperature = app.read()
  json = jsonify(current_temperature.__dict__)
  return json

