---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: num_theory/Eulers_totient_function.py
    title: num_theory/Eulers_totient_function.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_D


    from num_theory.Eulers_totient_function import Eulers_totient_function


    N = int(input())

    print(Eulers_totient_function(N))

    '
  dependsOn:
  - num_theory/Eulers_totient_function.py
  isVerificationFile: true
  path: verify-check/AOJ-NTL-1-D.test.py
  requiredBy: []
  timestamp: '2023-09-17 18:47:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify-check/AOJ-NTL-1-D.test.py
layout: document
redirect_from:
- /verify/verify-check/AOJ-NTL-1-D.test.py
- /verify/verify-check/AOJ-NTL-1-D.test.py.html
title: verify-check/AOJ-NTL-1-D.test.py
---
