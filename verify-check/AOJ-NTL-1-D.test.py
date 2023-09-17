# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_D

from num_theory.Eulers_totient_function import Eulers_totient_function

N = int(input())
print(Eulers_totient_function(N))
