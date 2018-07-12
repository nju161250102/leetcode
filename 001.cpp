#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    int length = nums.size();
    for (int i = 0; i < length-1; i++) {
        for (int j = i+1; j < length; j++) {
            if (nums[i] + nums[j] == target) {
                vector<int> result;
                result.push_back(i);
                result.push_back(j);
                return result;
            }
        }
    }
}

int main() {
	int nums[4] = {2, 7, 11, 15};
	vector<int> v(nums, nums+4);
	twoSum(v, 9);
}
