---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\ndef efficient_space_sieve(n):\n    sqrt_n = math.isqrt(n)\n\
    \    is_prime_small = [True] * (sqrt_n + 1)\n    is_prime_small[0] = is_prime_small[1]\
    \ = False\n\n    for i in range(2, int(math.sqrt(sqrt_n)) + 1):\n        if not\
    \ is_prime_small[i]:\n            continue\n        for j in range(i * i, sqrt_n\
    \ + 1, i):\n            is_prime_small[j] = False\n\n    primes = []\n    m =\
    \ (n + sqrt_n - 1) // sqrt_n\n    for s in range(1, m + 1):\n        a = (s -\
    \ 1) * sqrt_n\n        b = s * sqrt_n\n        is_prime = [True] * (b - a)\n\n\
    \        for i in range(2, int(math.sqrt(sqrt_n)) + 1):\n            if not is_prime_small[i]:\n\
    \                continue\n            k = max(i, (a + i - 1) // i)\n        \
    \    for j in range(k * i, b, i):\n                is_prime[j - a] = False\n\n\
    \        for i in range(b - a):\n            if is_prime[i] and i + a >= 2 and\
    \ i + a <= n:\n                primes.append(i + a)\n\n    return is_prime_small\n\
    \n#N = int(input())\n#print(efficient_space_sieve(N))\n"
  dependsOn: []
  isVerificationFile: false
  path: num_theory/Eratosthenes' interval sieve_all.py
  requiredBy: []
  timestamp: '2023-10-08 16:47:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num_theory/Eratosthenes' interval sieve_all.py
layout: document
redirect_from:
- /library/num_theory/Eratosthenes' interval sieve_all.py
- /library/num_theory/Eratosthenes' interval sieve_all.py.html
title: num_theory/Eratosthenes' interval sieve_all.py
---
