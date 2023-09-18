---
title: 繰り返し二乗法（C++）
documentation_of: ./num_theory/pow.cpp
---

# 概要
繰り返し二乗法を行います。


# 計算量
指数を $N$ として
- $O(logN)$

# 補足
Pythonなら下記コードで自動的に繰り返し二乗法を行ってくれる。
$a^b$を $mod$ で割った余りを $O(log(b))$ で出してくれる。

```Python:pow.py
pow(a,b,mod)
```
