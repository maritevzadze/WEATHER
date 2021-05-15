import requests
import json
import sqlite3

conn = sqlite3.connect('weather_db.sqlite3')
cursor = conn.cursor()
city = 'kutaisi'
key = 'b0382a9da8d31051dd5eecdc220673dc'
payload = {'q': city, 'appid': key,}
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}',params=payload)
print(r)
print(r.headers)
print(r.status_code)
print(r.text)
res = r.json()
print(type(res))
res = json.loads(r.text)
print(res)
print(type(res))
print(json.dumps(res, indent=4))
with open('data.json', 'w') as f:
    json.dump(res, f, indent=4)
temp_min = res['main']['temp_min']
print('მინიმალური ტემპერატურა: ',temp_min, 'C')
print('წნეხი: ', res['main']['pressure'], '%')

for each in res['weather']:
    weather.id_list.append(each[çountry])
    country = each['country']
    main = each['weather.main']
    description = each['weather.description']

cursor.execute('''CREATE TABLE weather
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               country VARCHAR(40))''')
cursor.execute('INSERT INTO weather(country,weather.main,weather.description) VALUES (?, ?, ?,)', )

conn.commit()
