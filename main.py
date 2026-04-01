from logger import log_system_data
from analyzer import analyze_logs
from visualize import show_graph

def main():
    while True:
        print("\n===== SYSTEM MONITOR =====")
        print("1. Log System Data")
        print("2. Analyze Logs")
        print("3. show Graph")
        print("4, Exit")       

        choice = input("Enter choice: ")

        if choice == "1":
            log_system_data()
        elif choice == "2":
            analyze_logs()
        elif choice == "3":
            show_graph()
        elif choice == "4":
             break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()