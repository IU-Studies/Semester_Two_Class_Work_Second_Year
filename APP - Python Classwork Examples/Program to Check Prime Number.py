#Program to Check Prime Number

def check_prime(number):
    num_range = number // 2
    count = 0
    for i in range(2, num_range):
        if number % i == 0:
            count += 1
    if count > 0:
        return f"{number} is not a Prime Number"
    else:
        return f"{number} is a Prime Number"

user_input = int(input("Enter a number:- "))

result = check_prime(user_input)

print(result)
