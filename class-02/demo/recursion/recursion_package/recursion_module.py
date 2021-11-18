# Use this function to recursively calculate the final factorial value
def factorial(n):
    # When we countdown to 1 we are done
    if n <= 1:
        isOne = 1
        print(f'{isOne}')    
        return isOne

    print(f'{n} * ')
    return (n * factorial(n - 1))

# Get the end number for factorial
inputNumber = int(input("enter a number: "));
print(f'factorial for {inputNumber} is {factorial(inputNumber)}')

