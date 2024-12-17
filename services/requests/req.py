import requests
import time
import random
fuel_type=['Petrol','Diesel','CNG']
trans=['Automatic','Manual']
seller=['Dealer','Individual']
for i in range(50):
    params = {'car_id': i}
    data = {
        "Car_Name": "ciaz",
        "Year": random.randint(2003,2018),
        "Present_Price": random.uniform(2,10),
        "Driven_kms": random.randint(5000,45000),
        "Fuel_Type": random.choice(fuel_type),
        "Selling_type": random.choice(seller),
        "Transmission": random.choice(trans),
        "Owner": random.randint(0,3)
        } 
    response = requests.post('http://price-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())