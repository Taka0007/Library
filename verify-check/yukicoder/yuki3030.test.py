# verification-helper: PROBLEM https://yukicoder.me/problems/no/3030

import random
from num_theory.Miller_Rabin import is_prime_miller_rabin

N = int(input())

for i in range(N):
    num = int(input())
    if is_prime_miller_rabin(num):
        ans = 1
    else:
        ans = 0
        
    print(num,ans,sep=' ')
