// https://leetcode.com/problems/powx-n/
// Time: O(n logn)
#include <iostream>
#include <cmath>

using namespace std;

double helper(double x, int n) {
    if (n == 0 || n == 1) {
        return x;
    }

    if (x == 0) {
        return 1;
    }

    if(n % 2 == 1) {
        return pow(x, n-1) * x;
    } else {
        double p = pow(x, n/2);

        return p*p;
    }
}

double pow(double x, int n) {
    if (x == 0 || n == 1) {
        return x;
    }
    if (n == 0) {
        return 1;
    }

    if (n < 0) {
        n = abs(n);
        x = 1 / x;
    }

    return helper(x, n);
}

int main() {
    double x;
    int n;
    cin >> x >> n;

    cout << pow(x, n) << endl;

    return 0;
}