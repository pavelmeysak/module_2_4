numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i != 1:
        for j in range(2,i):
            check = i % j
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
        else:
            not_primes.append(i)
print(f'Простые числа: {primes}')
print(f'Составные числа: {not_primes}')