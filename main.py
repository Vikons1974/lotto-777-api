from flask import Flask, Response
from parser import get_latest_csv
from flask_cors import CORS  # 👈 добавляем

app = Flask(__name__)
CORS(app)  # 👈 разрешаем CORS для всех маршрутов

@app.route("/")
def home():
    return "Lotto 777 API is running."

@app.route("/777.csv")
def get_csv():
    try:
        csv_data = get_latest_csv()
        return Response(csv_data, mimetype="text/csv")
    except Exception as e:
        return f"Ошибка при получении CSV: {str(e)}", 500
