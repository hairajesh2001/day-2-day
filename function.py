def product_of_two_numbers(a,b):
    print(a*b)

product_of_two_numbers(1,2)


product = product_of_two_numbers(4,2)
print(product) # print None because function not return any values


maximum = max (1,2,3,4) #built-in function
print(maximum)



def product_of_two_numbers(a,b):
    product = a * b;
    return product
 
print(product_of_two_numbers(2,3))  # prints 6


def calculate_sum_of_three_numbers(a, b, c):
    sum = a + b + c
    return sum

print(calculate_sum_of_three_numbers(1,4,5))


def calculate_cube(a):
    cube=a*a*a
    return cube

print(calculate_cube(5))
