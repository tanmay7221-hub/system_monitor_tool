import psutil
import csv
from datetime import datetime
import os

def log_system_data():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    time = datetime.now()

    file_exists = os.path.isfile("logs.csv")

    with open("logs.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "cpu", "ram"])

        writer.writerow([time, cpu, ram])

    print("Data Logged Successfully!")