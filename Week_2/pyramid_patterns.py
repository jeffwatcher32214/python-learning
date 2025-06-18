# Print a pyramid patterns
rows = 5
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(' ' * spaces + '*' * stars)

# Generate a multiplication table matrix (1–10 × 1–10)
size = 10

print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:>4}", end="")
print()

print("   " + "-" * (size * 4))

for row in range(1, size + 1):
    print(f"{row:>2} |", end="")
    for col in range(1, size + 1):
        product = row * col
        print(f"{product:>4}", end="")
    print()