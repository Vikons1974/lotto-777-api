import requests
from bs4 import BeautifulSoup
import csv
import io

def get_latest_csv():
    url = "https://www.pais.co.il/777/archive.aspx"
    headers = {"User-Agent": "Mozilla/5.0"}

    session = requests.Session()
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", {"id": "tblArchive"})

    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    rows = table.find_all("tr")
    for row in rows:
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if cells:
            writer.writerow(cells)

    return output.getvalue()
