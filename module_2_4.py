numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
n = 0
for i in numbers:
    print(i)
for j in range(len(numbers)):
    is_prime = True
    n = numbers[j]
    if n < 2:
        print(n, " не простое и не сложное")
        continue
    else:
        a = n ** (1 / 2)
    for k in range(2, int(a + 1)):
        if n % k == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
print("Primes: ", primes)
print("Not Primes: ", not_primes)