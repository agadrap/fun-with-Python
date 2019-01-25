def eratosthenes(num):
    mult = []
    primes = []
    for i in range(2, num+1):
        if i not in mult:
            primes.append(i)
            for j in range(i*i, num+1, i):
                mult.append(j)
    return primes
