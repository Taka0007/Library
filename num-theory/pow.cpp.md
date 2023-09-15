---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B
  bundledCode: "#line 1 \"num-theory/pow.cpp\"\n#define PROBLEM \"https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B\"\
    \n#include <iostream>\nusing namespace std;\n\nconst long long MOD = 1000000007;\
    \  // 10^9 + 7\n\nlong long mod_pow(long long base, long long exp, long long mod)\
    \ {\n    long long result = 1;\n    while (exp > 0) {\n        if (exp % 2 ==\
    \ 1) {\n            result = (result * base) % mod;\n        }\n        base =\
    \ (base * base) % mod;\n        exp /= 2;\n    }\n    return result;\n}\n\nint\
    \ main() {\n    long long m, n;\n    cin >> m >> n;\n    long long ans = mod_pow(m,\
    \ n, MOD);\n    cout << ans << endl;\n    return 0;\n}\n"
  code: "#define PROBLEM \"https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B\"\
    \n#include <iostream>\nusing namespace std;\n\nconst long long MOD = 1000000007;\
    \  // 10^9 + 7\n\nlong long mod_pow(long long base, long long exp, long long mod)\
    \ {\n    long long result = 1;\n    while (exp > 0) {\n        if (exp % 2 ==\
    \ 1) {\n            result = (result * base) % mod;\n        }\n        base =\
    \ (base * base) % mod;\n        exp /= 2;\n    }\n    return result;\n}\n\nint\
    \ main() {\n    long long m, n;\n    cin >> m >> n;\n    long long ans = mod_pow(m,\
    \ n, MOD);\n    cout << ans << endl;\n    return 0;\n}\n"
  dependsOn: []
  isVerificationFile: false
  path: num-theory/pow.cpp
  requiredBy: []
  timestamp: '2023-09-15 16:19:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num-theory/pow.cpp
layout: document
redirect_from:
- /library/num-theory/pow.cpp
- /library/num-theory/pow.cpp.html
title: num-theory/pow.cpp
---
