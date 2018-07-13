#include <iostream>
#include <string>
using namespace std;

string longestPalindrome(string s) {
	//暴力求解法 
	string sub = s.substr(0, 1);
    for (int length = s.size(); length >= 2; length --) {
    	for (int i = 0; i <= s.size() - length; i++) {
    		string str = s.substr(i, length);
    		cout << "test:" << str << endl;
    		bool flag = true;
    		for (int k = 0; k < str.size(); k++) {
    			if (str[k] != str[str.size()-k-1]) {
    				flag = false;
    				break;
				}
			}
			if (flag) return str;
		}
	}
	return sub;
}

int main() {
	cout << longestPalindrome("babad") << endl;
	cout << longestPalindrome("cbbd") << endl;
}
