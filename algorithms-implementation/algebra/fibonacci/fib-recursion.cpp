// Time: Fib(n) = Fib(n-1) + Fib(n-2) Which is exponential time.O(c^n)

#include <iostream>

using namespace std;

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}

int main() {
    int n;
    cin >> n;

    cout << fib(n) << endl;
    return 0;
}