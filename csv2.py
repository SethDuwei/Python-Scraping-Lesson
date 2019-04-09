import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    "https://en.wikipedia.org/wiki/Comparison_of_text_editors")
soup = BeautifulSoup(html, "lxml")
table = soup.find("table", {"class": "wikitable sortable"})
# print(table)
# th_data = []
csv_file = open("wiki.csv", "wt", encoding='utf-8')
writer = csv.writer(csv_file)
th_data = table.find_all(["th", "td"])
csv_row = []
for th_data_text in th_data:
    csv_row.append(th_data_text.get_text())
    # print(th_data_text.get_text())
# writer.writerow(csv_row)
print(csv_row)
