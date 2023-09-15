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
  bundledCode: "#line 1 \"num-theory/pow.cpp\"\n#include <iostream>\nusing namespace\
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
  path: num-theory/pow.cpp
  requiredBy: []
  timestamp: '2023-09-15 22:54:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify-check/AOJ-NTL-1-B.test.cpp
documentation_of: num-theory/pow.cpp
layout: document
redirect_from:
- /library/num-theory/pow.cpp
- /library/num-theory/pow.cpp.html
title: num-theory/pow.cpp
---
