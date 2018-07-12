#include <string>
#include <iostream>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int left = 0, right = 0; 			//���ַ���ǰ��λ���α� 
    int maxLength = 0; 					//��¼��󳤶� 
    if (s.size() <= 1) return s.size(); //����������� 
    for (int i = 1; i < s.size(); i++) {
        char c = s[i];
        for (int j = left; j <= right; j++) {
        	//���ǰ����Ӵ��������ַ����ƶ�ǰ�α� 
        	if (s[j] == c) {
        		if (right - left + 1 > maxLength) maxLength = right - left + 1;
				left = j+1;
        		break;
			}
		}
		right ++;	
    }
    //������󳤶� 
    if (right - left + 1 > maxLength) maxLength = right - left + 1;
    return maxLength;
}

int main() {
	cout << lengthOfLongestSubstring("abcabcbb") << endl;
	cout << lengthOfLongestSubstring("bbbbb") << endl;
	cout << lengthOfLongestSubstring("pwwkew") << endl;
	return 0;
}
