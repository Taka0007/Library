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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# \u30EB\u30B8\u30E3\u30F3\u30C9\u30EB\u95A2\u6570\uFF1A N! \u304C\u7D20\u6570\
    \ p \u3067\u4F55\u56DE\u5272\u308C\u308B\u304B\u3092\u6C42\u3081\u308B\ndef legendre(N,\
    \ p):\n    res = 0\n    while N > 0:\n        res += N // p\n        N //= p\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: num_theory/Legendre-function.py
  requiredBy: []
  timestamp: '2023-10-04 14:54:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num_theory/Legendre-function.py
layout: document
redirect_from:
- /library/num_theory/Legendre-function.py
- /library/num_theory/Legendre-function.py.html
title: num_theory/Legendre-function.py
---
