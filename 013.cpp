#include <iostream>
#include <string>
using namespace std;

int romanCharToInt(char c) {
	switch (c) {
		case 'I': return 1;
		case 'V': return 5;
		case 'X': return 10;
		case 'L': return 50;
		case 'C': return 100;
		case 'D': return 500;
		case 'M': return 1000;
	}
	return 0;
}

int romanToInt(string s) {
	int sum = 0;
    for (int i = 0; i < s.size() - 1; i++) {
    	int m = romanCharToInt(s[i]);
    	int n = romanCharToInt(s[i+1]);
    	if (m < n) sum -= m;
    	else sum += m;
	}
	sum += romanCharToInt(s[s.size()-1]);
	return sum;
}

int main() {
	cout << romanToInt("LVIII") << endl;	//58
	cout << romanToInt("MCMXCIV") << endl;	//1994
	return 0;
}
