#include <math>
using namespace std;

int maxArea(vector<int>& height) {
    int max = 0;
    for (int i = 0; i < height.size(); i++) {
        if (max > height[i] * (height.size() -i)) continue;
        for (int j = i; j < height.size(); j++) {
            int h = min(height[i], height[j]);
            if (h*(j-i) > max) max = h*(j-i);
        }
    }
    return max;
}
