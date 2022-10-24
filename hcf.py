# Made on 2.10.22

def find_prime_numbers(point, prime_numbers = None, start = 2):
    if prime_numbers == None: prime_numbers = []
    try:
        for i in range(start, point + 1):
            prime = True
            for point in prime_numbers:
                if i % point == 0:
                    prime = False
                    break
                else: prime = True
            if prime == True: prime_numbers.append(i)
    except: pass
    return prime_numbers

def prime_divide(number, possible_dividers,prime_numbers, point):
    while True:
        possible_dividers_copy = possible_dividers.copy()
        for prime_num in possible_dividers_copy:
            if number % prime_num == 0:
                return possible_dividers, prime_numbers, point
            possible_dividers.pop(0)
        prime_numbers = find_prime_numbers(point + 10, prime_numbers)
        for num in prime_numbers:
            if num < point: possible_dividers.append(num)
        point += 10

def find_factors(number):
    point_till_primes_know = 10
    prime_factors = []
    prime_numbers = find_prime_numbers(point_till_primes_know)
    possible_dividers = prime_numbers.copy()
    while number != 1:
        possible_dividers, prime_numbers, point = prime_divide(number, possible_dividers, prime_numbers,point_till_primes_know)
        prime_factors.append(possible_dividers[0])
        number /= possible_dividers[0]
    prime_factors.append(1)
    return prime_factors

numbers = []
numbers_prime_factors = []
x = int(input("How many numbers do you want to find the HCF of? "))
for i in range(x):
    inp = int(input(f"Enter number {i+1}: "))
    numbers.append(inp)
    factors = find_factors(inp)
    if i >= 1: common_numbers = set(common_numbers).intersection(factors)
    else: common_numbers = factors
sum = 1
for num in common_numbers: sum *= num
input(f"The HCF is: {sum}")