#include <iostream>

using namespace std;

int maxMin(int k, vector<int> arr) {
    int n = arr.size();
    sort(arr.begin(), arr.end());
    int answer = INT_MAX;

    for (int i = 0; i + k -1 < n; i++) {
        answer = min(answer, arr[i+k-1] - arr[i]);
    }

    return answer;
}

int main() {
    cout << maxMin(3, {10, 100, 300, 200, 1000, 20, 30 }) << endl;
}