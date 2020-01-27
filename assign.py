'''Function to find the max of three numbers'''

def max_numbers(numbers):
    max_number = -1
    for x in numbers:
        if x > max_number:
            max_number = x
        else:
            continue
    return max_number
numbers = [34,98,70]
print(max_numbers(numbers))



'''Function that accepts a string and calculates the upper case letters and lower case letters'''

def case_count():
    lower_case_count = 0
    upper_case_count = 0
    string = input('please enter a sentence: ')
    for letter in string:
        if letter.isupper():
            upper_case_count += 1
        elif letter.islower():
            lower_case_count += 1
    solution = 'The number of upper case letters is {0} and lower case letters is {1}'.format(upper_case_count,
                                                                                             lower_case_count)
    return solution
print(case_count())


'''Function to test if a number is a prime number'''

def prime_checker(num):
    if num >= 2:
        for y in range(2, num):
            if not (num % y):
                return '{} is not a prime number'.format(num)
    else:
        return '{} is not a prime number'.format(num)
    return '{} is a prime number'.format(num)

print(prime_checker(9))'''Function to find the max of three numbers'''

def max_numbers(numbers):
    max_number = -1
    for x in numbers:
        if x > max_number:
            max_number = x
        else:
            continue
    return max_number
numbers = [34,98,70]
print(max_numbers(numbers))



'''Function that accepts a string and calculates the upper case letters and lower case letters'''

def case_count():
    lower_case_count = 0
    upper_case_count = 0
    string = input('please enter a sentence: ')
    for letter in string:
        if letter.isupper():
            upper_case_count += 1
        elif letter.islower():
            lower_case_count += 1
    solution = 'The number of upper case letters is {0} and lower case letters is {1}'.format(upper_case_count,
                                                                                             lower_case_count)
    return solution
print(case_count())


'''Function to test if a number is a prime number'''

def prime_checker(num):
    if num >= 2:
        for y in range(2, num):
            if not (num % y):
                return '{} is not a prime number'.format(num)
    else:
        return '{} is not a prime number'.format(num)
    return '{} is a prime number'.format(num)

print(prime_checker(9))
