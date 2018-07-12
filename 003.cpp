#include <string>
#include <iostream>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int left = 0, right = 0; 			//子字符串前后位置游标 
    int maxLength = 0; 					//记录最大长度 
    if (s.size() <= 1) return s.size(); //特殊情况处理 
    for (int i = 1; i < s.size(); i++) {
        char c = s[i];
        for (int j = left; j <= right; j++) {
        	//如果前面的子串包含该字符，移动前游标 
        	if (s[j] == c) {
        		if (right - left + 1 > maxLength) maxLength = right - left + 1;
				left = j+1;
        		break;
			}
		}
		right ++;	
    }
    //更新最大长度 
    if (right - left + 1 > maxLength) maxLength = right - left + 1;
    return maxLength;
}

int main() {
	cout << lengthOfLongestSubstring("abcabcbb") << endl;
	cout << lengthOfLongestSubstring("bbbbb") << endl;
	cout << lengthOfLongestSubstring("pwwkew") << endl;
	return 0;
}
