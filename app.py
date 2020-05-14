import requests as rq
from bs4 import BeautifulSoup
from table import print_table
from noti import send

def template(data):
    body = []
    for i in range(0, data['count']):
        body.append([data['Country'][i], data['Total case'][i], data['New case'][i], data['Total deaths'][i], data['New deaths'][i], data['Recovered'][i], data['Active cases'][i]])
    return '<code>' + '\n'.join(print_table(body, ["Country", "Total case", "New case", "Total deaths", "New deaths", "Recovered", "Active cases"], 150, 7)) + '</code>'

# BASE_URL = "https://www.worldometers.info/coronavirus/country/us/"
BASE_URL = "https://www.worldometers.info/coronavirus/#c-all%22"

res = rq.get(BASE_URL)
soup = BeautifulSoup(res.content, 'html.parser')

# total = soup.select('.total_row_usa td')
total = soup.select('.total_row_world td')
result= {
    "Country" :["North America"],
    "Total case" : [str(total[1].text)],
    "New case" : [str(total[2].text)],
    "Total deaths" : [str(total[3].text)],
    "New deaths" : [str(total[4].text)],
    "Recovered" : [str(total[5].text)],
    "Active cases" : [str(total[6].text)],
    'count' : 1
}
table_rows = soup.select('.row tbody tr')

for row in table_rows[8:40]: # supposed to be until 222 but because of telegram message limitation
    tds = row.select('td')
    result["Country"].append(tds[0].text)
    result["Total case"].append(tds[1].text)
    result["New case"].append(tds[2].text)
    result["Total deaths"].append(tds[3].text)
    result["New deaths"].append(tds[4].text)
    result["Recovered"].append(tds[5].text)
    result["Active cases"].append(tds[6].text)
    result['count'] += 1
for row in table_rows[49:50]: # supposed to be until 222 but because of telegram message limitation
    tds = row.select('td')
    result["Country"].append(tds[0].text)
    result["Total case"].append(tds[1].text)
    result["New case"].append(tds[2].text)
    result["Total deaths"].append(tds[3].text)
    result["New deaths"].append(tds[4].text)
    result["Recovered"].append(tds[5].text)
    result["Active cases"].append(tds[6].text)
    result['count'] += 1
for row in table_rows[229:230]: # World Total count
    tds = row.select('td')
    result["Country"].append("World")
    result["Total case"].append(tds[1].text)
    result["New case"].append(tds[2].text)
    result["Total deaths"].append(tds[3].text)
    result["New deaths"].append(tds[4].text)
    result["Recovered"].append(tds[5].text)
    result["Active cases"].append(tds[6].text)
    result['count'] += 1

data = template(result)
print(data)

helper = '''

Column Description:
-Country: Countries in the World
-Total case: Number of total cases
-New case: Number of new cases
-Total deaths: Number of total deaths
-New deaths: Number of new deaths
-Recovered: Number of the recovered
-Active case: Number of people not cured
'''

send(data + helper)

