#include <iostream>

using namespace std;

int fib(int n) {
    if (n <= 1) return n;

    return fib(n-1) + fib(n-2);
}

int main() {
    int num;
    cin >> num;
    if (num <= 30) {
        cout << fib(num) << endl;
    }
    return 0;
}