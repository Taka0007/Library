---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: num_theory/Eulers_totient_function.cpp
    title: num_theory/Eulers_totient_function.cpp
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: cpp
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    '*NOT_SPECIAL_COMMENTS*': ''
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D
  bundledCode: "#line 1 \"verify-check/AOJ-NTL-1-D.test.cpp\"\n#define PROBLEM \"\
    https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D\"\n#include <iostream>\n#line\
    \ 1 \"num_theory/Eulers_totient_function.cpp\"\nint Eulers_Totient_Function(int\
    \ N) {\n    // \u521D\u671F\u5024\n    int result = N;\n\n    // \u7D20\u56E0\u6570\
    \u5206\u89E3\u7528\u306E\u6570\u5B57\n    int num = 2;\n\n    // num\u304CN\u306E\
    \u5E73\u65B9\u6839\u4EE5\u4E0B\u306B\u306A\u308B\u307E\u3067\u7E70\u308A\u8FD4\
    \u3057\n    while (num * num <= N) {\n        // num\u304Cresult\u306E\u56E0\u6570\
    \u306E\u5834\u5408\u306F\u03C6\u95A2\u6570\u306B\u64CD\u4F5C\u3092\u884C\u3046\
    \n        if (N % num == 0) {\n            result = (result / num) * (num - 1);\n\
    \n            // num\u3092\u56E0\u6570\u306B\u542B\u3093\u3067\u3044\u308B\u9650\
    \u308A\u64CD\u4F5C\u3092\u884C\u3044\u3001N\u306B\u542B\u307E\u308C\u308B\u56E0\
    \u6570num\u3092\u306A\u304F\u3057\u3066\u3044\u308B\n            while (N % num\
    \ == 0) {\n                N /= num;\n            }\n        }\n\n        // num\u3092\
    \u5909\u66F4\u3057\u3066\u6B21\u306E\u7D20\u56E0\u6570\u3092\u63A2\u3059\n   \
    \     num++;\n    }\n\n    // \u307E\u3060\u7D20\u56E0\u6570\u304C\u6B8B\u3063\
    \u3066\u3044\u308B\u5834\u5408\u3001\u03C6\u95A2\u6570\u3092\u64CD\u4F5C\u3059\
    \u308B\n    if (N > 1) {\n        result = (result / N) * (N - 1);\n    }\n\n\
    \    return result;\n}\n#line 4 \"verify-check/AOJ-NTL-1-D.test.cpp\"\nusing namespace\
    \ std;\nint main() {\n    int N;\n    cin >> N;\n    cout << Eulers_Totient_Function(N)\
    \ << endl;\n    return 0;\n}\n"
  code: "#define PROBLEM \"https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D\"\n#include\
    \ <iostream>\n#include \"num_theory/Eulers_totient_function.cpp\"\nusing namespace\
    \ std;\nint main() {\n    int N;\n    cin >> N;\n    cout << Eulers_Totient_Function(N)\
    \ << endl;\n    return 0;\n}\n"
  dependsOn:
  - num_theory/Eulers_totient_function.cpp
  isVerificationFile: true
  path: verify-check/AOJ-NTL-1-D.test.cpp
  requiredBy: []
  timestamp: '2023-09-17 19:02:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify-check/AOJ-NTL-1-D.test.cpp
layout: document
redirect_from:
- /verify/verify-check/AOJ-NTL-1-D.test.cpp
- /verify/verify-check/AOJ-NTL-1-D.test.cpp.html
title: verify-check/AOJ-NTL-1-D.test.cpp
---
