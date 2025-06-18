# FizzBuzz Challenge, Print numbers 1–100, For multiples of 3, print "Fizz", For multiples of 5, print "Buzz", For both, print "FizzBuzz"
for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        print(f"Number {i}: FizzBuzz")
    if i%5 == 0:
        print(f"Number {i}: Buzz")
    if i%3 == 0:
        print(f"Number {i}: Fizz")