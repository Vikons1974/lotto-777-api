import requests
import csv
from io import StringIO

def get_latest_csv():
    url = "https://media.pais.co.il/api/pages/777/archive?year=2025"
    response = requests.get(url)

    if response.status_code != 200:
        return "Ошибка при получении данных от API"

    data = response.json()

    # Проверка структуры
    if "data" not in data or "table" not in data["data"]:
        return "Неверный формат данных от API"

    records = data["data"]["table"]["body"]

    output = StringIO()
    writer = csv.writer(output, delimiter=';')

    # Формируем CSV: заголовки + строки
    for row in records:
        # row["numbers"] – это список чисел (иногда 17, иногда меньше)
        numbers = row.get("numbers", [])
        # Заполним недостающие числа нулями
        numbers += ["" for _ in range(17 - len(numbers))]
        writer.writerow(numbers)

    return output.getvalue()
