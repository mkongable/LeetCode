def maximum69Number (self, num):
    # Convert num to a string
    # Loop through the string
    # Switch the first 6 found with 9
    # Convert the string back to an integer
    # Return the integer
    num = str(num)
    for i in range(len(num)):
        if num[i] == '6':
            num = num[:i] + '9' + num[i+1:]
            break
    return int(num)
