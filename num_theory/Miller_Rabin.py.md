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
  code: "import random\n\ndef is_prime_miller_rabin(n, k=10):\n    if n <= 1:\n  \
    \      return False\n    if n <= 3:\n        return True\n\n    # n - 1\u3092\
    \ (2^r) * d \u306B\u5206\u89E3\u3059\u308B\n    r, d = 0, n - 1\n    while d %\
    \ 2 == 0:\n        r += 1\n        d //= 2\n\n    # \u30DF\u30E9\u30FC\u30E9\u30D3\
    \u30F3\u30C6\u30B9\u30C8\u3092k\u56DE\u7E70\u308A\u8FD4\u3059\n    for _ in range(k):\n\
    \        a = random.randint(2, n - 2)\n        x = pow(a, d, n)\n\n        if\
    \ x == 1 or x == n - 1:\n            continue\n\n        for _ in range(r - 1):\n\
    \            x = pow(x, 2, n)\n            if x == n - 1:\n                break\n\
    \        else:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: num_theory/Miller_Rabin.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num_theory/Miller_Rabin.py
layout: document
redirect_from:
- /library/num_theory/Miller_Rabin.py
- /library/num_theory/Miller_Rabin.py.html
title: num_theory/Miller_Rabin.py
---
