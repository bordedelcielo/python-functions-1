# EXERCISE 1
# Cube Number Test... 
# Print out all cubed numbers up to the total value 1000. 
# Meaning that if the cubed number is over 1000 break the loop.

# While the cubed number (a variable) is greater than or equal to 1000, keep running the program.

def cubed_range(input_number):
    cubic_root = 1
    print_list = []
    while cubic_root ** 3 <= input_number:
        print_list.append(cubic_root ** 3)
        cubic_root += 1
    return print_list

print(cubed_range(1000))

# EXERCISE 2
# Get first prime numbers up to 100
# HINT:
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

# My helper function
def is_prime(input_number):
    for number in range(3,input_number,2):
        # print(f'Here is number: {number}.')

        if input_number % number == 0:
            # print(f'Here is number: {number}. input_number is not prime.')
            # print(f'{input_number} is not a prime number because it is divisible by {number}.')
            return False
    
    # print(f'{input_number} is a prime number. It is not divisble by any number except itself and one.')
    return True
    
# print(is_prime(7))

# The overall function
def get_primes(input_number):

    list_of_prime_numbers = [2]

    for item in range(3,input_number+1,2):
        if is_prime(item) == True:
            list_of_prime_numbers.append(item)
    
    return list_of_prime_numbers

print(get_primes(100))

# Exercise 3
# Take in a users input for their age, 
# if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

def age_category_from_input():

    program_running = True

    while program_running == True:
        age = int(input('Please confirm your age to determine your category, or enter \'0\' to quit this program.'))
        if age == 0:
            program_running = False
            print('Have a nice day!')
        if age < 18:
            print('kids')
        elif age < 66:
            print('adults')
        else:
            print('seniors')

age_category_from_input()