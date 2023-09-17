int Eulers_Totient_Function(int N) {
    // 初期値
    int result = N;

    // 素因数分解用の数字
    int num = 2;

    // numがNの平方根以下になるまで繰り返し
    while (num * num <= N) {
        // numがresultの因数の場合はφ関数に操作を行う
        if (N % num == 0) {
            result = (result / num) * (num - 1);

            // numを因数に含んでいる限り操作を行い、Nに含まれる因数numをなくしている
            while (N % num == 0) {
                N /= num;
            }
        }

        // numを変更して次の素因数を探す
        num++;
    }

    // まだ素因数が残っている場合、φ関数を操作する
    if (N > 1) {
        result = (result / N) * (N - 1);
    }

    return result;
}
