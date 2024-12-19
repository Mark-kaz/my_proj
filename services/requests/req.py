import requests
import time
import random

for i in range(50):  # Отправляем 50 запросов
    params = {'flat_id': i}  # Уникальный ID объекта
    data = {
       "Car_Name": "Honda Activa 4G",
        "Year": 2017,
        "Present_Price": random.randint(5, 20),
        "Driven_kms": random.randint(1, 200000),
        "Fuel_Type": "Petrol",
        "Selling_type": "Individual",
        "Transmission": "Automatic",
        "Owner": 0
    }
    # Отправляем POST-запрос
    response = requests.post('http://price-predict:8000/api/prediction', params=params, json=data)
    # Печатаем ответ
    print(response.json())
    # Пауза от 0 до 5 секунд
    time.sleep(random.uniform(0, 5))