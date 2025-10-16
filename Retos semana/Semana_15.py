import requests

latitud = 19.387274
longitud = -99.142271
API_KEY = '0932ed7aed5aef2c2914a9cc3ace2ee5'

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={API_KEY}&units=metric&lang=es'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print(f"Temperatura: {data['main']['temp']}°C")
    print(f"Descripción: {data['weather'][0]['description']}")
    print(f"Humedad: {data['main']['humidity']}%")
else:
    print("Error al obtener datos:", response.status_code)