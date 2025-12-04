from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action, log_file=LOG_PATH):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_file", "a") as file:
        file.write(f"[{timestamp}] {action}\n")

def search_logs(keyword, log_file=LOG_PATH):
    try:
        with open("log_file", "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log File not found.")

log_action("User logged in")
log_action("User updated profile")
search_logs("profile")