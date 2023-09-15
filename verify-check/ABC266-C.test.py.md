---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc266/tasks/abc266_c
    links:
    - https://atcoder.jp/contests/abc266/tasks/abc266_c
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.5/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# IGNORE\n# verification-helper: PROBLEM https://atcoder.jp/contests/abc266/tasks/abc266_c\n\
    from scipy.spatial import ConvexHull\na1,a2 = map(int,input().split())\nb1,b2\
    \ = map(int,input().split())\nc1,c2 = map(int,input().split())\nd1,d2 = map(int,input().split())\n\
    \npoints = [ [a1,a2],[b1,b2], [c1,c2], [d1,d2] ]\nhull = ConvexHull(points)\n\
    points = hull.points\nhull_points = points[hull.vertices]\n\nif len(hull_points)==4:\n\
    \    ans = 'Yes'\nelse:\n    ans = 'No'\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: verify-check/ABC266-C.test.py
  requiredBy: []
  timestamp: '2023-09-16 01:11:12+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: verify-check/ABC266-C.test.py
layout: document
redirect_from:
- /verify/verify-check/ABC266-C.test.py
- /verify/verify-check/ABC266-C.test.py.html
title: verify-check/ABC266-C.test.py
---
