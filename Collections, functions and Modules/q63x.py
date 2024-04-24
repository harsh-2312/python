# Write a Python program to returns sum of all divisors of a number 

# def div(num):
#     divnum=[1]
#     for i in range(2,num):
#         if num % i ==0:
#             divnum.append(i)
#     return sum(divnum)

# num=int(input("enter number:"))

# print(div(num))

def sum_of_divisors(n):
    # Initialize sum
    result = 0

    # Find divisors and add them
    for i in range(1, n + 1):
        if n % i == 0:
            result += i

    return result

# Test the function
num = int(input("Enter a number: "))
print("Sum of divisors:", sum_of_divisors(num))
