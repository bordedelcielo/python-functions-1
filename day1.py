def cubed_range(input_number):
    cubic_root = 1
    print_list = []
    while cubic_root ** 3 <= input_number:
        print_list.append(cubic_root ** 3)
        cubic_root += 1
    return print_list
print(cubed_range(1000))

def is_prime(input_number):
    for number in range(3,input_number,2):
        if input_number % number == 0:
            return False
    return True

def get_primes(input_number):
    list_of_prime_numbers = [2]
    for item in range(3,input_number+1,2):
        if is_prime(item) == True:
            list_of_prime_numbers.append(item)
    return list_of_prime_numbers
print(get_primes(100))

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