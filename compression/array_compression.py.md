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
  code: "# \u4E8C\u5206\u63A2\u7D22\u306E\u5B9A\u7FA9\ndef binary_search(array, target):\n\
    \    left, right = 0, len(array) - 1\n\n    while left <= right:\n        mid\
    \ = (left + right) // 2\n\n        if array[mid] == target:\n            return\
    \ mid\n        elif array[mid] < target:\n            left = mid + 1\n       \
    \ else:\n            right = mid - 1\n    return -1\n\n\nN = int(input())\nA =\
    \ list(map(int,input().split()))\n\n# \u5EA7\u6A19\u5727\u7E2E\u5F8C\u306E\u914D\
    \u5217\u306E\u5B9A\u7FA9\nB = [0]*N\n\n# \u5143\u306E\u914D\u5217\u306E\u91CD\u8907\
    \u3092\u524A\u9664\u3057\u3001\u30BD\u30FC\u30C8\u3057\u305F\u914D\u5217T\u306E\
    \u5BA3\u8A00\nT = list(set(A))\nT.sort()\n\nfor i in range(N):\n    B[i] = binary_search(T,A[i])\n\
    \    B[i] += 1\nprint(*B)\n"
  dependsOn: []
  isVerificationFile: false
  path: compression/array_compression.py
  requiredBy: []
  timestamp: '2023-10-09 20:06:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: compression/array_compression.py
layout: document
title: "\u5EA7\u6A19\u5727\u7E2E"
---

# 概要
座標圧縮を行います。

# 計算量
- 未解析（後で書きます。）

# 補足
Pythonならmap関連の動作が早いので、これでも通る。
```Python : array_compression.py
N = int(input())
A = list(map(int, input().split()))
sorted_unique_A = sorted(set(A))
coordinate_map = {value: index + 1 for index, value in enumerate(sorted_unique_A)}
B = [coordinate_map[a] for a in A]
print(*B)
```
