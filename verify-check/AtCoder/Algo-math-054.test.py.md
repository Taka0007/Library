---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_at
    links:
    - https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_at
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_at\n\
    \n\nimport numpy as np\n\ndef dot(A1, A2, N, mod):\n    # N: \u884C\u5217\u306E\
    \u30B5\u30A4\u30BA\n    A = np.zeros((N, N), dtype=int)\n    for i in range(N):\n\
    \        for j in range(N):\n            for k in range(N):\n                A[i][j]\
    \ = (A[i][j] + (A1[i][k] * A2[k][j]) % mod) % mod\n    return A\n\ndef pow_mat(A,\
    \ K, N, mod):\n    # A: \u7D2F\u4E57\u3059\u308B\u884C\u5217, k: \u7D2F\u4E57\u6570\
    , n: \u884C\u5217A\u306E\u30B5\u30A4\u30BA\n    P = np.eye(N, dtype=int)\n   \
    \ while K:\n        if K & 1:\n            P = dot(P, A, N, mod)\n        A =\
    \ dot(A, A, N, mod)\n        K >>= 1\n    return P\n\nN = int(input())\nmat =\
    \ np.array([[1, 1], [1, 0]], dtype=int)\nmod = 10**9\nans_matrix = pow_mat(mat,\
    \ N-1, 2, mod)\nans = (ans_matrix[1][0] + ans_matrix[1][1]) % mod\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: verify-check/AtCoder/Algo-math-054.test.py
  requiredBy: []
  timestamp: '2023-09-21 14:28:58+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: verify-check/AtCoder/Algo-math-054.test.py
layout: document
redirect_from:
- /verify/verify-check/AtCoder/Algo-math-054.test.py
- /verify/verify-check/AtCoder/Algo-math-054.test.py.html
title: verify-check/AtCoder/Algo-math-054.test.py
---
