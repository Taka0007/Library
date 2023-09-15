#define PROBLEM "https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B"
#include <iostream>
using namespace std;

const long long MOD = 1000000007;  // 10^9 + 7

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    long long m, n;
    cin >> m >> n;
    long long ans = mod_pow(m, n, MOD);
    cout << ans << endl;
    return 0;
}
