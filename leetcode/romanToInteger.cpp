//https://www.mathsisfun.com/roman-numerals.html is explanation of roman numerals;
/*
    [Adding] The value of each symbol is added from left to right;
    [SUBTRACTING] When there is a smaller number placed before a larger number;
*/ 
#include <iostream>
#include <map>

using namespace std;

struct Solution {
    
    int romanToInt(string s) {
        map<char, int> m = {{'I', 1}, {'V', 5},{'X', 10},{'L', 50},
        {'C', 100},{'D', 500},{'M', 1000}};
        
        int total = 0;
        for(int i = 0; i < s.length(); i++){
            if(m[s[i+1]] <= m[s[i]])  total += m[s[i]]; 
            else  total -= m[s[i]];  
        }
        return total;
    }
};

int main() {
    Solution s;
    cout << s.romanToInt("X");
    return 0;
}