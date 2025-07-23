from datetime import datetime

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {action}\n")

if __name__ == "__main__":
    log_action("Started program")
    log_action("Added student John")
    log_action("Viewed all students")
    print("Log actions saved to log.txt")
