print("Welcome to Python Learning")

#input example 
#variable name  = input ("Enter Name")

username = input("Enter your user name:")

print("Welcome", username)

def print_username_using_function(username):
    print( "Hello",username)


print_username_using_function (username)

number_a = int(input("enter a number:"))
number_b = int(input("enter a number:"))
def product_of_two_numbers(a , b):
    if a == b:
        print(a , "and" ,b ,"are equal" )
        a = "equal"
        return a
    else:
        print(a,b, "are not equal")
        a = "not equal"
        return a
    

a = product_of_two_numbers(number_a,number_b)

print(a)
