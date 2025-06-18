# Print the first 10 natural numbers using for and while
for i in range(1, 11):
    print(i)

i=0
while (i <= 10):
    print(i)
    i += 1

# Calculate the sum of numbers from 1 to 100
sum = 0
for i in range (1, 101):
    sum +=i
print(sum)

# Print multiplication tables from 1 to 10
mul = 0
for i in range (1, 11):
    print(f"Table of {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print('-' * 15)

# Create a countdown timer from 10 to 1
for i in range (10, 0, -1):
    print(i)
print("Countdown Complete!")

# Use break to exit a loop when a condition is met
for i in range(1,11):
    if i == 5:
        print("Condition met! Loop breaking!")
        break

# Use continue to skip odd numbers and print only even numbers
for i in range(1, 51):
    if i %2 != 0:
        continue
    print(i)

# Use pass to define an empty loop or conditional placeholder
for i in range(0, 10):
    pass
print("pass")

# Create a list of student names, use enumerate() to display roll numbers Generate: Even numbers from 0 to 50
names = ["James", "Emily", "Michael", "Olivia", "William", "Sophia", "David", "Isabella", "John", "Mia",
         "Robert", "Charlotte", "Joseph", "Amelia", "Thomas", "Harper", "Daniel", "Abigail", "Matthew", "Evelyn", 
         "Anthony", "Elizabeth", "Mark", "Sofia", "Donald", "Avery", "Paul", "Ella", "Steven", "Scarlett",
         "Andrew", "Grace", "Joshua", "Chloe", "Kenneth", "Victoria", "Kevin", "Lily", "Brian", "Hannah",
         "George", "Lillian", "Edward", "Natalie", "Ronald", "Zoe", "Timothy", "Leah", "Jason", "Stella",
         "Jeffrey", "Aubrey", "Ryan", "Addison", "Jacob", "Lucy", "Gary", "Brooklyn", "Nicholas", "Audrey",
         "Eric", "Bella", "Stephen", "Claire", "Jonathan", "Skylar", "Larry", "Savannah", "Justin", "Penelope",
         "Scott", "Aria", "Brandon", "Camila", "Frank", "Violet", "Benjamin", "Ellie", "Samuel", "Paisley",
         "Gregory", "Nora", "Patrick", "Hazel", "Raymond", "Aurora", "Dennis", "Riley", "Jerry", "Luna",
         "Tyler", "Layla", "Aaron", "Alexa", "Peter", "Samantha", "Henry", "Allison", "Adam", "Elena"]
for i, name in enumerate(names):
    if i <= 50:
        if i%2 == 0:
            print(f"Even Roll Number: {i} {name}")
    else:
        break

# Create a list of student names, use enumerate() to display roll numbers Generate: Odd numbers from 51 to 100
names = ["James", "Emily", "Michael", "Olivia", "William", "Sophia", "David", "Isabella", "John", "Mia",
         "Robert", "Charlotte", "Joseph", "Amelia", "Thomas", "Harper", "Daniel", "Abigail", "Matthew", "Evelyn", 
         "Anthony", "Elizabeth", "Mark", "Sofia", "Donald", "Avery", "Paul", "Ella", "Steven", "Scarlett",
         "Andrew", "Grace", "Joshua", "Chloe", "Kenneth", "Victoria", "Kevin", "Lily", "Brian", "Hannah",
         "George", "Lillian", "Edward", "Natalie", "Ronald", "Zoe", "Timothy", "Leah", "Jason", "Stella",
         "Jeffrey", "Aubrey", "Ryan", "Addison", "Jacob", "Lucy", "Gary", "Brooklyn", "Nicholas", "Audrey",
         "Eric", "Bella", "Stephen", "Claire", "Jonathan", "Skylar", "Larry", "Savannah", "Justin", "Penelope",
         "Scott", "Aria", "Brandon", "Camila", "Frank", "Violet", "Benjamin", "Ellie", "Samuel", "Paisley",
         "Gregory", "Nora", "Patrick", "Hazel", "Raymond", "Aurora", "Dennis", "Riley", "Jerry", "Luna",
         "Tyler", "Layla", "Aaron", "Alexa", "Peter", "Samantha", "Henry", "Allison", "Adam", "Elena"]
for i, name in enumerate(names):
    if i > 50:
        if i%2 != 0:
            print(f"Odd Roll Number: {i} {name}")
    else:
        continue

# Create a list of student names, use enumerate() to display roll numbers Generate: Squares of numbers 1–10 using list comprehension with range()
for i in range(1, 11):
    print(f"Square of Number {i}: {i*i}")