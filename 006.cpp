#include <iostream>
#include <string>
using namespace std;

string convert(string s, int numRows) {
	string result = "";
	if (numRows == 1) return s;
    for (int i = 0; i < numRows; i++) {
    	if (i == 0 || i == numRows-1) {
    		for (int j = i; j < s.size(); j += (numRows*2 - 2)) {
    			result += s[j];
			}
		} else {
			int k = i*2;
			for (int j = i; j < s.size(); ) {
				result += s[j];
				k = numRows*2 - 2 - k;
				j += k;
			}
		}
    	
	}
	return result;
}

int main() {
	cout << convert("A", 1) << endl;
	cout << convert("PAYPALISHIRING", 4) << endl;
	return 0;
}
