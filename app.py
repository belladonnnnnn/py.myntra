import sys
import os
from flask import Flask, request, jsonify
import pandas as pd

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(_file_)))

from model.forecasting_model import TrendDemandForecast

app = Flask(_name_)

# Load historical data
trends_data = pd.read_csv('data/trends.csv')

# Initialize forecasting model
forecast_model = TrendDemandForecast(trends_data)

@app.route('/forecast', methods=['GET'])
def forecast():
    product_id = request.args.get('product_id')
    forecast = forecast_model.predict(product_id)
    return jsonify(forecast)

@app.route('/add_post', methods=['POST'])
def add_post():
    post_data = request.json
    # Here you would normally save to a database
    return jsonify({"message": "Post added successfully", "post": post_data}), 201

if _name_ == '_main_':
    app.run(debug=True)
