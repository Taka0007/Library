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
  code: "def Eulers_totient_function(N):\n    # \u521D\u671F\u5024\n    result = N\n\
    \    \n    # \u7D20\u56E0\u6570\u5206\u89E3\u7528\u306E\u6570\u5B57\n    num =\
    \ 2\n    \n    # num\u304CN**(1/2)\u306B\u306A\u308B\u307E\u3067\u7E70\u308A\u8FD4\
    \u3057\n    while num**2 <= N:\n        # num\u304Cresult\u306E\u56E0\u6570\u306E\
    \u5834\u5408\u306F\u03C6\u95A2\u6570\u306B\u64CD\u4F5C\u3092\u884C\u3046\n   \
    \     if N%num==0:\n            result = (result//num)*(num-1)\n            \n\
    \            # num\u3092\u56E0\u6570\u306B\u542B\u3093\u3067\u3044\u308B\u9650\
    \u308A\u64CD\u4F5C\u3092\u884C\u3044\u3001N\u306B\u542B\u307E\u308C\u308B\u56E0\
    \u6570num\u3092\u306A\u304F\u3057\u3066\u3044\u308B\n            while N%num==0:\n\
    \                N//=num\n                \n        # num\u3092\u5909\u66F4\u3057\
    \u3066\u6B21\u306E\u7D20\u56E0\u6570\u3092\u63A2\u3059\n        num += 1\n   \
    \     \n    # \u307E\u3060\u7D20\u56E0\u6570\u304C\u6B8B\u3063\u3066\u3044\u308B\
    \u5834\u5408\u3001\u03C6\u95A2\u6570\u3092\u64CD\u4F5C\u3059\u308B\n    if N>1:\n\
    \        result = (result//N)*(N-1)\n    \n    return result\n"
  dependsOn: []
  isVerificationFile: false
  path: num-theory/Eulers_totient_function.py
  requiredBy: []
  timestamp: '2023-09-17 18:34:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num-theory/Eulers_totient_function.py
layout: document
redirect_from:
- /library/num-theory/Eulers_totient_function.py
- /library/num-theory/Eulers_totient_function.py.html
title: num-theory/Eulers_totient_function.py
---
