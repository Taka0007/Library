#define PROBLEM "https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B"
#include <iostream>
#include "num-theory/pow.cpp"
using namespace std;
int main() {
    long long m, n;
    cin >> m >> n;
    long long ans = mod_pow(m, n, MOD);
    cout << ans << endl;
    return 0;
}
