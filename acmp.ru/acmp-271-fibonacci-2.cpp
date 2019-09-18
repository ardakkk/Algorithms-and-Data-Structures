#include <iostream>

using namespace std;

int main() {
    int n, a = 0, b = 1, c, index = 0;
    cin >> n;

    for (int i = 2; i < n; i++) {
        a = b;
        b = c;
        c = a + b;
        index++;
    }

    if(c == n) cout << 1 << endl << index;

    else cout << 0;

    return 0;
}