---
title: オイラーのφ関数（Python）
documentation_of: ./num_theory/Eulers_totient_function.py
---

# 積集合
オイラーのφ関数を返します。

# 計算量


# 補足
sympyを使っていいなら下記コードのほうが断然早い

```Python
from sympy import totient

n = 546354743765756756464
result = totient(n)
print(result)
```
