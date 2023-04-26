n = int(input("Check the prime number: "))

def prime_checker(number=n):
    is_prime =True
    for i in range(2, number):
        if number % i== 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker()