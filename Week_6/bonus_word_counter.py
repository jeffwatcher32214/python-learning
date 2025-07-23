def word_counter(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            lines = text.strip().split('\n')
            words = text.split()
            characters = len(text)

            print(f"File: {filename}")
            print(f"Lines: {len(lines)}")
            print(f"Words: {len(words)}")
            print(f"Characters: {characters}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    word_counter("students_data.txt")
