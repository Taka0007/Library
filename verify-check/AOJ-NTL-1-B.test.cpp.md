---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: num_theory/pow.cpp
    title: num_theory/pow.cpp
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    '*NOT_SPECIAL_COMMENTS*': ''
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B
  bundledCode: "#line 1 \"verify-check/AOJ-NTL-1-B.test.cpp\"\n#define PROBLEM \"\
    https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B\"\n#include <iostream>\n\
    #line 2 \"num_theory/pow.cpp\"\nusing namespace std;\n\nconst long long MOD =\
    \ 1000000007;  // 10^9 + 7\n\nlong long mod_pow(long long base, long long exp,\
    \ long long mod) {\n    long long result = 1;\n    while (exp > 0) {\n       \
    \ if (exp % 2 == 1) {\n            result = (result * base) % mod;\n        }\n\
    \        base = (base * base) % mod;\n        exp /= 2;\n    }\n    return result;\n\
    }\n#line 4 \"verify-check/AOJ-NTL-1-B.test.cpp\"\nusing namespace std;\nint main()\
    \ {\n    long long m, n;\n    cin >> m >> n;\n    long long ans = mod_pow(m, n,\
    \ MOD);\n    cout << ans << endl;\n    return 0;\n}\n"
  code: "#define PROBLEM \"https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B\"\
    \n#include <iostream>\n#include \"num_theory/pow.cpp\"\nusing namespace std;\n\
    int main() {\n    long long m, n;\n    cin >> m >> n;\n    long long ans = mod_pow(m,\
    \ n, MOD);\n    cout << ans << endl;\n    return 0;\n}\n"
  dependsOn:
  - num_theory/pow.cpp
  isVerificationFile: true
  path: verify-check/AOJ-NTL-1-B.test.cpp
  requiredBy: []
  timestamp: '2023-09-17 18:49:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify-check/AOJ-NTL-1-B.test.cpp
layout: document
redirect_from:
- /verify/verify-check/AOJ-NTL-1-B.test.cpp
- /verify/verify-check/AOJ-NTL-1-B.test.cpp.html
title: verify-check/AOJ-NTL-1-B.test.cpp
---
