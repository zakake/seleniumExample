def is_prime(number):
    """ Return True if the number is prime """
    for element in range(number):
        if(element > 1) and (number % element == 0):
            return False
    return True
