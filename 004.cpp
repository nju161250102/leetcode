#include <iostream>
#include <vector>
using namespace std;
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    int m = nums2.size();
    int i = 0, j = 0;
    vector<int> v;
    if (m + n == 0) return 0;
    //合并两个vector 
    while (1) {
        if (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                v.push_back(nums1[i]);
                i++;
            } else {
                v.push_back(nums2[j]);
                j++;
            }
        } else if (i < n && j == m) {
            v.push_back(nums1[i]);
            i++;
        } else if (i == n && j < m) {
            v.push_back(nums2[j]);
            j++;
        } else break;
    }
    //求中位数 
    if ((n+m) % 2 == 1) {
        return v[v.size()/2]*1.0;
    } else return (v[v.size()/2] + v[v.size()/2-1])/2.0;
}

int main() {
	vector<int> nums1;
	int num2[1] = {2};
	vector<int> nums2(num2, num2+1);
	vector<int>& a = nums1;
	vector<int>& b = nums2;
	cout << findMedianSortedArrays(a, b) << endl;
	return 0;
} 
