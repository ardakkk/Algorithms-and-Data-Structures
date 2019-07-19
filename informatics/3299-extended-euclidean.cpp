#include <iostream>

using namespace std;

int gcd(int a, int b, int & x, int  & y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }

    int x1, y1;

    int d = gcd(b%a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;

    return d;
}

int main() {
    int a, b, c, x, y;
    cin >> a >> b >> c;

    bool isALessThanB = true;

    if (a > b) {
        isALessThanB = false;
        int tmp = a;
        a = b;
        b = tmp;
    }

    int g = gcd(a, b, x, y);

    if (!isALessThanB) {
        int tmp = x;
        x = y;
        y = tmp;
    }

    cout << g << ' ' << x * c / g << ' ' << y * c / g << endl;

    return 0;
}