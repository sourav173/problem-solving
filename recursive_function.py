'''
problem: create recursive function to calculate the factorial of a number
'''

# normal factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120

# factorial using recursive function
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)


print(recursive_factorial(5))