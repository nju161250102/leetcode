#include <iostream>
#include <string>
#include <vector>
using namespace std;

string longestPrefix(vector<string>::iterator begin, vector<string>::iterator end) {
	if (end == begin) return "";
	if (end - begin == 1) return *begin;
	else {
		int half = (end - begin) / 2;
		string leftStr = longestPrefix(begin, begin + half);
		string rightStr = longestPrefix(begin + half, end);
		for (int i = 0; i < leftStr.size(); i++) {
			if (i == rightStr.size()) return rightStr;
			if (leftStr[i] != rightStr[i]) return leftStr.substr(0, i);
		}
		return leftStr;
	}
}

string longestCommonPrefix(vector<string>& strs) {
	return longestPrefix(strs.begin(), strs.end());
}

int main() {
	vector<string> v;
	v.push_back("flower");
	v.push_back("flow");
	v.push_back("flight");
	cout << longestCommonPrefix(v);
	return 0;
}
