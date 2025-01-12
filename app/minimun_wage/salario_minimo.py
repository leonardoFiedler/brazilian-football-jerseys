from bs4 import BeautifulSoup
import requests
import csv

# Realiza o download do site IPEADATA
r = requests.get("http://www.ipeadata.gov.br/ExibeSerie.aspx?stub=1&serid1739471028=1739471028")

soup = BeautifulSoup(r.text, "html.parser")

items = soup.find_all("tr", class_="dxgvDataRow")

l_sal = []

out_file = open('salario_minimo_historico.csv', 'w')
writer = csv.writer(out_file, quoting=csv.QUOTE_MINIMAL)

writer.writerow(["ano", "mes", "valor"])

for item in items:
    td = item.find_all("td")
    
    if len(td) > 1:
        date_sal = td[0].text.split(".")
        
        year = int(date_sal[0])
        
        # Grab only for 2013 and following
        if year < 2013:
            continue
        
        value_sal = td[1].text.replace(".", "").replace(",", ".")
        
        writer.writerow([year, int(date_sal[1]), float(value_sal)])

out_file.close()
