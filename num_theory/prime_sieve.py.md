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
  code: "# \u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9\n# N\u307E\u3067\
    \u306E\u7D20\u6570\u3092\u5217\u6319\u3059\u308B\ndef prime_sieve(N):\n    \n\
    \    # N\u307E\u3067\u306E\u6570\u5217\u3092\u4F5C\u6210\u3002True\u306A\u3089\
    \u305D\u306E\u6570\u5B57\u306F\u7D20\u6570\u3002\n    num = [True]*(N+1)\n   \
    \ \n    # 0,1\u306F\u7D20\u6570\u3067\u306A\u3044\u306E\u30671\u306B\u3057\u3066\
    \u304A\u304F\n    num[0] = False\n    num[1] = False\n    # 1\uFF5EN\u307E\u3067\
    \u306E\u7BC4\u56F2\u3092\u8D70\u67FB\u3002\n    # 1-index\u3067\u8003\u3048\u307E\
    \u3059\u3002 (ex:1\u306Fnum[1],77\u306Fnum[77])\n    for i in range(2,N+1):\n\
    \        if num[i]:\n            # i\u304C\u7D20\u6570\u3067\u3042\u308B\u5834\
    \u5408\u3001i\u306E\u500D\u6570\u306E\u30D5\u30E9\u30B0\u3092\u5168\u30661\u306B\
    \u5909\u66F4\u3059\u308B\n            for j in range(2*i, N+1, i):\n         \
    \       num[j] = False\n    return num\n\nN   = int(input())\nnum = prime_sieve(N+2)\n\
    \nans = sum(num[:N+1])\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: false
  path: num_theory/prime_sieve.py
  requiredBy: []
  timestamp: '2023-09-22 16:18:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: num_theory/prime_sieve.py
layout: document
title: "\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\u7BE9(Python)"
---

# 概要
エラトステネスの篩を行い、N以下の数が素数かどうかを格納したリストを返します。（ここら辺の説明については拡充予定）<br>
余りにNが大きすぎるとメモリエラーが出るので注意。

# 計算量

# Verify問題
- アルゴ式：https://algo-method.com/submissions/1147166
