---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
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
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num_theory/pow.cpp
layout: document
redirect_from:
- /library/num_theory/pow.cpp
- /library/num_theory/pow.cpp.html
title: num_theory/pow.cpp
---
