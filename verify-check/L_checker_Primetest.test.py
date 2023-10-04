# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test

from num_theory.Miller_Rabin import is_prime_miller_rabin


Q = int(input())
for i in range(Q):
    N = int(input())
    if is_prime_miller_rabin(N):
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
