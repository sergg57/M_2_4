numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    for j in range(1, numbers[i] + 1):
        if j != 1 and j != numbers[i] and (numbers[i] % j) == 0:
            is_prime = False
    if is_prime == True:
        if numbers[i] != 1:
            primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('Primes = ', primes)
print('Not Primes = ', not_primes)
