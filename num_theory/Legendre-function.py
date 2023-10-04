# ルジャンドル関数： N! が素数 p で何回割れるかを求める
def legendre(N, p):
    res = 0
    while N > 0:
        res += N // p
        N //= p
    return res
