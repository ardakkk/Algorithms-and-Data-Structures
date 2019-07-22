#include <iostream>
using namespace std;

int main() {
    int x, y, z, w;
    cin >> x >> y >> z >> w;

    int cnt=0;
    for(int i=0;i<=1000;i++)
    {
        for(int j=0;j<=1000;j++)
        {
            if(x*i+y*j<=w && (w-x*i-y*j)%z==0)
            {
                cnt++;
            }
        }
    }

    cout << cnt;

    return 0;
}