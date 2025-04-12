from flask import Flask, Response
from parser import get_latest_csv

app = Flask(__name__)

@app.route('/')
def home():
    return "777 Neo API — работает!"

@app.route('/777.csv')
def get_csv():
    csv_data = get_latest_csv()
    return Response(csv_data, mimetype='text/csv')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
