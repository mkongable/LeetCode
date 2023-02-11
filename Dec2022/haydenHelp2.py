num = input("Enter a number: ")

def factorial(num):
    # if num is less than or equal to 0, then it's not a valid input
    if num <= 0:
        print("Error: Invalid number entered.")
    # if positive, then calculate the factorial
    else:
        fact = 1
        # for each number from 1 to num, multiply the current factorial by the current number
        for i in range(1, num + 1): # 1 <= i < num + 1
            fact = fact * i
        return fact
    
    
print(factorial(int(num)))

# A factorial is the product of all positive integers less than or equal to the number.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
# 1*2*3*4*5 = 120