#include <iostream>
#include <math.h>
using namespace std;

int getNum(int x, int n) {
	int a = (int) pow(10, n+1);
	int b = (int) pow(10, n);
	return (x - x/a*a)/b;
}

bool isPalindrome(int x) {
	if (x < 0) return false;
	if (x < 10) return true;
    int m = 0;
    for (int i = x; i > 0; i /= 10) m++;
    for (int i = 0; i < m; i++) {
    	if (getNum(x, i) != getNum(x, m-i-1)) return false;
	}
	return true;
}

int main() {
	cout << isPalindrome(121) << endl;
	cout << isPalindrome(10) << endl;
}
