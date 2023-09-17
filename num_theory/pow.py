# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B
m,n = map(int,input().split())
mod = 10**9 + 7
ans = pow(m,n,mod)
print(ans)
