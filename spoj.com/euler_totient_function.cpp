#include <iostream>

using namespace std;

int phi(int n) {
    int result = n;

    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            result -= result / i;
        }
    }
    if (n > 1) {
        result -= result / n;
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    int nums[n];

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    for (int i = 0; i < n; i++) {
        cout << phi(nums[i]) << endl;
    }
    return 0;
}