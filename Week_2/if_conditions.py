# Check if a number is positive, negative, or zero
number  = 10
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print(f"{number} is Zero")

# Determine if someone is eligible to vote (age ≥ 18)
age = 17
if age >= 18:
    print("Person is eligible to Vote!")
else:
    print("Person is illigible to Vote!")

# Grade student marks using if-elif-else: Example Grading Scale: 90+ = A, 80–89 = B, 70–79 = C, <70 = F
grade = 90
if grade >= 90 and grade <= 100:
    print("A Grade!")
elif grade >= 80 and grade <= 89:
    print("B Grade!")
elif grade >= 70 and grade <= 79:
    print("C Grade!")
else:
    print("F Grade!")


# Write a program to check: If a number is even AND positive
number = 10
if number%2 == 0 and number > 0:
    print("Number is Even and Positive")
else:
    print("Either Number is not Even or Positive")


# Write a program to check: If a person qualifies for a loan: (age > 21 OR has guarantor) AND income > threshold
age_of_qualifier = 21
guarantor = True
income = 100
threshold = 50
if ((age > 21 or guarantor == True) and (income > threshold)):
    print("Person is qualified for loan!")
else:
    print("Person is not qualified for loan!")

# Create truth tables using combinations of boolean values manually
# Truth table generator
values = [True, False]

print(f"{'A':<6} {'B':<6} {'A AND B':<10} {'A OR B':<10} {'NOT A':<10}")
print("-" * 50)

for A in values:
    for B in values:
        print(f"{A:<6} {B:<6} {A and B:<10} {A or B:<10} {not A:<10}")
