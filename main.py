from pymongo import MongoClient
import json
from datetime import datetime
import time  # Import the time module for sleeping
import apscheduler 
import random

client = MongoClient('mongodb+srv://user_fyp:YxQNKAF8qYGSBHIT@cluster0.a5jdgea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
BASE_PATH="Power-Plant-Dashboard/json-db"
db = client['FYP']  

# Access your collections
demand_forecast_col = db['demand_forecast']
demand_col = db['demand']

def save_to_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, default=str)

def SaveData(type, data):
    data_Category = [dt['date_time'] for dt in data]
    data_series = [dt['demand'] for dt in data]

    save_to_file(f"{BASE_PATH}/{type}_Category.json", data_Category)
    save_to_file(f"{BASE_PATH}/{type}_series.json", data_series)

# Function to process and save data for a given collection, type, and skip value
def process_and_save_data(collection, data_type, skip_amount):
    data = []
    for doc in collection.find().sort("date_time", 1).skip(skip_amount).limit(10):
        if 'date_time' in doc:
            doc['date_time'] = datetime.strptime(doc['date_time'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S.000Z')
        data.append(doc)
    SaveData(data_type, data)
    print(f"Processed and saved {data_type} with skip {skip_amount}")

for i in range(0, 50):  
    process_and_save_data(demand_forecast_col, "data_forecast", i )
    process_and_save_data(demand_col, "data_demand", i )

    time.sleep(0.8)  

  


