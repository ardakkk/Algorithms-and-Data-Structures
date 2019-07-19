#include <iostream>

using namespace std;

int gcd(int a, int b, int & x, int & y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return d;
}

int main() {
    int a, b, x, y;
    cin >> a >> b;

    if (b > a) {
        int temp;
        temp = a;
        a = b;
        b = temp;
    }

    cout << gcd(a, b, x, y) << endl;

    return 0;
}