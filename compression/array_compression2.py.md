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
  code: "N = int(input())\nA = list(map(int, input().split()))\n\n# \u91CD\u8907\u524A\
    \u9664&\u30BD\u30FC\u30C8\nsorted_unique_A = sorted(set(A))\n\n# \u5EA7\u6A19\u5727\
    \u7E2E\u30DE\u30C3\u30D7\ncoordinate_map = {value: index + 1 for index, value\
    \ in enumerate(sorted_unique_A)}\n\n# \u5EA7\u6A19\u5727\u7E2E\u3092\u884C\u3044\
    \u3001B\u306B\u683C\u7D0D\nB = [coordinate_map[a] for a in A]\n\nprint(*B)\n"
  dependsOn: []
  isVerificationFile: false
  path: compression/array_compression2.py
  requiredBy: []
  timestamp: '2023-10-09 20:07:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: compression/array_compression2.py
layout: document
redirect_from:
- /library/compression/array_compression2.py
- /library/compression/array_compression2.py.html
title: compression/array_compression2.py
---
