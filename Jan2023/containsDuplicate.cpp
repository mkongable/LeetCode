#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int i = 0; i < nums.size(); i++) {
        if (seen.find(nums[i]) != seen.end()) {
            return true;
        }
        seen.insert(nums[i]);
    }
    return false;
}

int main() {
    vector<int> nums = {1,2,3,1};
    cout << containsDuplicate(nums) << endl;
    return 0;
}