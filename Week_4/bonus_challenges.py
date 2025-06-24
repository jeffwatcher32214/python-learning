# Merge two lists into a dictionary (keys from one list, values from other list).
keys = ["name", "age", "country"]
values = ["John", 25, "USA"]

merged_dict = dict(zip(keys, values))

print(merged_dict)

# Find duplicates in a list using sets.
numbers = [1, 2, 3, 4, 5, 2, 4, 6, 7, 3, 8, 9, 10, 5]

duplicates = set()

seen = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(f"Duplicates: {duplicates}")

# Create a word frequency counter for any given sentence.
sentence = "Python is very very easy and very very powerful"

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")