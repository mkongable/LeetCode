#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int pivotIndex(vector<int>& nums) {
    int leftSum = 0;
    int result = -1;
    //right sum = the sum of all elements
    int rightSum = 0;

    for (int i = 0; i < nums.size(); i++) {
        rightSum += nums[i];
    }

    //do a scan through the array, decreasing rightSum and increasing leftSum
    for (int i = 0; i < nums.size(); i++) {
        rightSum -= nums[i];
        if (leftSum == rightSum) {
            result = i;
            break;
        }
        leftSum += nums[i];
    }

    return result;
}

int main() {
    vector<int> nums = {1,7,3,6,5,6};
    cout << pivotIndex(nums) << endl;
    return 0;
}