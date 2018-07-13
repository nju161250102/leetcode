#include <iostream>
#include <string>
using namespace std;

int myAtoi(string str) {
	long long result = 0;
    int k = 1;
    bool lock = true;
    for (int i = 0; i < str.size(); i++) {
        char c = str[i];
        if (c == ' ' && lock) {
            continue;
        } else {
            if (c >= '0' && c <= '9') {
                if (lock) lock = false;
                result = result*10 + (c - 48);
                if (result*k < INT_MIN) return INT_MIN;
                if (result*k > INT_MAX) return INT_MAX;
            } else if (c == '-' && lock) {
                lock = false;
                k = -1;
            } else if (c == '+' && lock) {
                lock = false;
            }
            else break;
        }
    }
    return result*k; 
}

int main() {
	cout << myAtoi("   -42") << endl;
	cout << myAtoi("4193 with words") << endl;
	cout << myAtoi("words and 987") << endl;
}

