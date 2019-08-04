// Time: O(log(n))
#include <iostream>

using namespace std;

int P[2][2] = {{0, 1}, {1, 1}};

int A[2][2] = {{0, 1}, {1, 1}};

int F[2][2] = {{0, 0}, {1, 0}};

void mult(int M1[2][2], int M2[2][2]) {
    int a = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0];
    int b = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1];
    int c = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0];
    int d = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1];

    M1[0][0] = a;
    M1[0][1] = b;
    M1[1][0] = c;
    M1[1][1] = d;
}

void power(int M[2][2], int n) {
    if (n == 0 || n == 1) return;

    if (n%2 != 0) {
        power(M, n -1);
        mult(M, A);
    } else {
        power(M, n / 2);
        mult(M, M);
    }
}

int fib(int n) {
    power(P, n);
    mult(F, P);

    return F[1][0];
}

int main() {
    int n;
    cin >> n;

    cout << fib(n+1);
    return 0;
}