# Create a new file and write 5 lines to it.
# Open and read the file content.
# Append 2 more lines to the file.
# Use with open(...) context manager for safe file operations.
# Read file line by line using a loop.
def write_file():
    with open("students.txt", mode='w') as file:
        file.write("John\n")
        file.write("Emily\n")
        file.write("Olivia\n")
        file.write("William\n")
        file.write("Noah\n")

def read_file():
    with open("students.txt", mode='r') as file:
        for line in file:
            student = line.strip()
            print(student)

def main():
    write_file()
    read_file()

if __name__ == "__main__":
    main()