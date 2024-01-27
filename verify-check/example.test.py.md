---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.1/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nclass UnionFindTree:\n    def\
    \ __init__(self, n):\n        self.par = list(range(n))  # parent\n        self.rank\
    \ = [0] * n  # depth of tree\n\n    def find(self, x):\n        if self.par[x]\
    \ == x:\n            return x\n        else:\n            self.par[x] = self.find(self.par[x])\n\
    \            return self.par[x]\n\n    def unite(self, x, y):\n        x, y =\
    \ self.find(x), self.find(y)\n        if x == y:\n            return\n       \
    \ if self.rank[x] < self.rank[y]:\n            self.par[x] = y\n        else:\n\
    \            self.par[y] = x\n            if self.rank[x] == self.rank[y]:\n \
    \               self.rank[x] += 1\n\n    def is_same(self, x, y):\n        return\
    \ self.find(x) == self.find(y)\n\n\ndef main() -> None:\n    N, Q = map(int, input().split())\n\
    \    uft = UnionFindTree(N)\n    for _ in range(Q):\n        t, u, v = map(int,\
    \ input().split())\n        if t == 0:\n            uft.unite(u, v)\n        else:\n\
    \            print(int(uft.is_same(u, v)))\n\n\nif __name__ == \"__main__\":\n\
    \    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: verify-check/example.test.py
  requiredBy: []
  timestamp: '2023-09-15 13:44:16+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify-check/example.test.py
layout: document
redirect_from:
- /verify/verify-check/example.test.py
- /verify/verify-check/example.test.py.html
title: verify-check/example.test.py
---
