---
title: 座標圧縮
documentation_of: ./compression/array_compression.py
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
