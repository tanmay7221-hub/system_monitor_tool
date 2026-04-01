import csv
import matplotlib.pyplot as plt

def show_graph():
    cpu_list = []
    ram_list = []

    with open("logs.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) < 3:
                continue
            cpu_list.append(float(row[1]))
            ram_list.append(float(row[2]))

    if not cpu_list:
        print("No data to visualize!")
        return

    plt.plot(cpu_list, label="CPU Usage (%)")
    plt.plot(ram_list, label="RAM Usage (%)")

    plt.title("System Usage Over Time")
    plt.xlabel("Entries")
    plt.ylabel("Usage (%)")
    plt.legend()

    plt.show()