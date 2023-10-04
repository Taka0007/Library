---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/primality_test
    links:
    - https://judge.yosupo.jp/problem/primality_test
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test\n\
    \nfrom num_theory.Miller_Rabin import is_prime_miller_rabin\n\n\nQ = int(input())\n\
    for i in range(Q):\n    N = int(input())\n    if is_prime_miller_rabin(N):\n \
    \       ans = 'Yes'\n    else:\n        ans = 'No'\n    print(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: verify-check/L_checker_Primetest.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify-check/L_checker_Primetest.test.py
layout: document
redirect_from:
- /verify/verify-check/L_checker_Primetest.test.py
- /verify/verify-check/L_checker_Primetest.test.py.html
title: verify-check/L_checker_Primetest.test.py
---
