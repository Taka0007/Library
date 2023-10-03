import math

def efficient_space_sieve(n):
    sqrt_n = math.isqrt(n)
    is_prime_small = [True] * (sqrt_n + 1)
    is_prime_small[0] = is_prime_small[1] = False

    for i in range(2, int(math.sqrt(sqrt_n)) + 1):
        if not is_prime_small[i]:
            continue
        for j in range(i * i, sqrt_n + 1, i):
            is_prime_small[j] = False

    primes = []
    m = (n + sqrt_n - 1) // sqrt_n
    for s in range(1, m + 1):
        a = (s - 1) * sqrt_n
        b = s * sqrt_n
        is_prime = [True] * (b - a)

        for i in range(2, int(math.sqrt(sqrt_n)) + 1):
            if not is_prime_small[i]:
                continue
            k = max(i, (a + i - 1) // i)
            for j in range(k * i, b, i):
                is_prime[j - a] = False

        for i in range(b - a):
            if is_prime[i] and i + a >= 2 and i + a <= n:
                primes.append(i + a)

    return is_prime_small

N = int(input())
print(efficient_space_sieve(N))
