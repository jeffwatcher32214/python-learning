# Create a function that accepts any list and returns: Max value
# Create a function that accepts any list and returns: Min value
# Create a function that accepts any list and returns: Average value
def list_statistics(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    average_value = sum(numbers) / len(numbers)
    
    return max_value, min_value, average_value

# Create a function to reverse a string.
def reverse_string(s):
    return s[::-1]

# Create a function to count vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def main():
    numbers = [4, 8, 15, 16, 23, 42]
    max_val, min_val, avg_val = list_statistics(numbers)
    print(f"Max: {max_val}")
    print(f"Min: {min_val}")
    print(f"Average: {avg_val}")

    word = "Python"
    reversed_word = reverse_string(word)
    print(f"Reversed: {reversed_word}")

    sentence = "Python is Awesome"
    vowel_count = count_vowels(sentence)
    print(f"Number of vowels: {vowel_count}")

if __name__ == "__main__":
    main()