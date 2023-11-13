test_primes = [2, 3, 5, 11, 13, 17, 19, 23]
test_not_primes = [1, 4, 8, 9, 15, 18, 21, 25]

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

for prime in test_primes:
    print(is_prime(prime))

for np in test_not_primes:
    print(not is_prime(np))
