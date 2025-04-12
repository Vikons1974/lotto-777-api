import requests
import csv
from io import StringIO

def get_latest_csv():
    try:
        url = "https://media.pais.co.il/api/pages/777/archive?year=2025"
        response = requests.get(url, timeout=10)

        print("✅ Ответ получен. Код:", response.status_code)

        if response.status_code != 200:
            return "Ошибка при получении данных от API"

        data = response.json()
        print("🔍 Ключи JSON:", list(data.keys()))

        if "data" not in data or "table" not in data["data"]:
            print("❌ Структура JSON изменилась!")
            return "Неверный формат данных от API"

        records = data["data"]["table"]["body"]
        print(f"📦 Найдено {len(records)} записей")

        output = StringIO()
        writer = csv.writer(output, delimiter=';')

        for row in records:
            numbers = row.get("numbers", [])
            numbers += ["" for _ in range(17 - len(numbers))]  # Заполнение до 17 чисел
            writer.writerow(numbers)

        print("✅ CSV успешно сформирован")
        return output.getvalue()

    except Exception as e:
        print("🔥 Ошибка:", str(e))
        return f"Ошибка: {str(e)}"
