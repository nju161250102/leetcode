#include <iostream>
using namespace std;

int reverse(int x) {
	long long result = 0;
	while(x != 0) {
		result = result*10 + x%10;
		x = (x - x%10) / 10;
	}
	if (result < INT_MIN || result > INT_MAX) return 0;
	return result;
}

int main() {
	cout << reverse(123) << endl;
	cout << reverse(-123) << endl;
	cout << reverse(1534236469) << endl;
	return 0;
}
