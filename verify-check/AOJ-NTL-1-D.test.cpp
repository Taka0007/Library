#define PROBLEM "https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_D"
#include <iostream>
#include "num_theory/Eulers_totient_function.cpp"
using namespace std;
int main() {
    int N;
    cin >> N;
    cout << EulersTotientFunction(N) << endl;
    return 0;
}
