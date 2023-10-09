---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify-check/AOJ-NTL-1-B.test.cpp
    title: verify-check/AOJ-NTL-1-B.test.cpp
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "#line 1 \"num_theory/pow.cpp\"\n#include <iostream>\nusing namespace\
    \ std;\n\nconst long long MOD = 1000000007;  // 10^9 + 7\n\nlong long mod_pow(long\
    \ long base, long long exp, long long mod) {\n    long long result = 1;\n    while\
    \ (exp > 0) {\n        if (exp % 2 == 1) {\n            result = (result * base)\
    \ % mod;\n        }\n        base = (base * base) % mod;\n        exp /= 2;\n\
    \    }\n    return result;\n}\n"
  code: "#include <iostream>\nusing namespace std;\n\nconst long long MOD = 1000000007;\
    \  // 10^9 + 7\n\nlong long mod_pow(long long base, long long exp, long long mod)\
    \ {\n    long long result = 1;\n    while (exp > 0) {\n        if (exp % 2 ==\
    \ 1) {\n            result = (result * base) % mod;\n        }\n        base =\
    \ (base * base) % mod;\n        exp /= 2;\n    }\n    return result;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: num_theory/pow.cpp
  requiredBy: []
  timestamp: '2023-09-17 18:47:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify-check/AOJ-NTL-1-B.test.cpp
documentation_of: num_theory/pow.cpp
layout: document
title: "\u7E70\u308A\u8FD4\u3057\u4E8C\u4E57\u6CD5\uFF08C++\uFF09"
---

# 概要
繰り返し二乗法を行います。


# 計算量

- 指数を $N$ として $O(logN)$

# 補足
Pythonなら下記コードで自動的に繰り返し二乗法を行ってくれる。
$a^b$を $mod$ で割った余りを $O(log(b))$ で出してくれる。

```Python:pow.py
pow(a,b,mod)
```