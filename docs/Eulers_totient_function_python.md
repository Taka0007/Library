---
title: オイラーのφ関数（Python）
documentation_of: ./num_theory/Eulers_totient_function.py
---

# 概要
オイラーのφ関数を返します。

# 計算量
- NULL

# 補足
sympyを使っていいなら下記コードのほうが断然早い

```Python:totient.py
from sympy import totient

n = int(input())
result = totient(n)
print(result)
```
