import csv

def analyze_logs():
    cpu_list = []
    ram_list = []

    try:
        with open("logs.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                cpu_list.append(float(row[1]))
                ram_list.append(float(row[2]))

        if len(cpu_list) == 0:
            print("No data available!")
            return

        print("\n📊 SYSTEM ANALYSIS")
        print("----------------------")
        print(f"Average CPU Usage: {sum(cpu_list)/len(cpu_list):.2f}%")
        print(f"Max CPU Usage: {max(cpu_list):.2f}%")
        print(f"Average RAM Usage: {sum(ram_list)/len(ram_list):.2f}%")
        print(f"Max RAM Usage: {max(ram_list):.2f}%")
        

    except FileNotFoundError:
        print("Log file not found!")