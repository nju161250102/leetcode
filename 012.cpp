#include <iostream>
#include <string>
#include <math.h>
using namespace std;

string intToRoman(int num) {
    string table[4][9] = {
        {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
        {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
        {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
        {"M", "MM", "MMM"}};
    string s = "";
    for (int i = 0; i < 4; i++) {
        int k = num - num / 10 * 10;
        if (k != 0) s = table[i][k-1] + s;
        num = (num - k)/10;
    }
    return s;
}
    
int main() {
	cout << intToRoman(58) << endl;		//LVIII
	cout << intToRoman(1994) << endl;	//MCMXCIV
	return 0;
} 
