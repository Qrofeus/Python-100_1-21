# Given code block:
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Solution:
for number in range(1, 101):
    # 'FizzBuzz' should only be printed if number is divisible by BOTH 3 AND 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # For a number only ONE of notation is allowed
    # Adding 'elif' and 'else' clauses skips all other comparisons if one has already been executed
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Removing square brackets for proper formatting
        print(number)
