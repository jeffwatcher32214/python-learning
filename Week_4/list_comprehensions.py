# Generate a list of squares from 1 to 20 using list comprehension.

# Generate a list of even numbers from 1 to 50 using list comprehension.

# Create a list of words from a sentence and filter only words longer than 5 letters using list comprehension.
def main():
    squares = []
    for x in range(1, 21):
        squares.append(x*x)
    print(f"Squares: {squares}")

    even = []
    for x in range(1, 51):
        if x%2 == 0:
            even.append(x)
    print(f"Even: {even}")

    sentence = "Python programming language is very powerful and enjoyable"
    words = sentence.split()
    print(f"Words: {words}")
    big_words = []
    for x in words:
        if len(x) > 5:
            big_words.append(x)
    print(f"Words of 6 or more Length: {big_words}")

if __name__ == "__main__":
    main()