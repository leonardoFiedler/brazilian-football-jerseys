from bs4 import BeautifulSoup
import requests
import csv

INPUT_URL = (
    "http://www.ipeadata.gov.br/ExibeSerie.aspx?stub=1&serid1739471028=1739471028"
)
OUTPUT_FILE = "data/processed/minimum_wage_historical.csv"

r = requests.get(INPUT_URL)

soup = BeautifulSoup(r.text, "html.parser")

items = soup.find_all("tr", class_="dxgvDataRow")

l_sal = []

y_dict = dict()

for item in items:
    td = item.find_all("td")

    if len(td) > 1:
        date_sal = td[0].text.split(".")

        year = int(date_sal[0])

        # Grab only for 2012 and following
        if year < 2012:
            continue

        value_sal = td[1].text.replace(".", "").replace(",", ".")

        if year in y_dict.keys():
            if value_sal > y_dict[year]:
                y_dict[year] = value_sal
        else:
            y_dict[year] = value_sal


out_file = open(OUTPUT_FILE, "w")
writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)

writer.writerow(["year", "value"])

for k, v in y_dict.items():
    writer.writerow([k, float(v)])

out_file.close()
