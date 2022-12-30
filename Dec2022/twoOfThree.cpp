#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <functional>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <array>
#include <bitset>

using namespace std;

vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
   // create a set of the numbers in nums1
    set<int> nums1Set;
    for (int i = 0; i < nums1.size(); i++) {
        nums1Set.insert(nums1[i]);
    }

    // create a set of the numbers in nums2
    set<int> nums2Set;
    for (int i = 0; i < nums2.size(); i++) {
        nums2Set.insert(nums2[i]);
    }

    // create a set of the numbers in nums3
    set<int> nums3Set;
    for (int i = 0; i < nums3.size(); i++) {
        nums3Set.insert(nums3[i]);
    }

    // create a set of the numbers that are in nums1 and nums2
    set<int> nums1And2;
    set_intersection(nums1Set.begin(), nums1Set.end(), nums2Set.begin(), nums2Set.end(), inserter(nums1And2, nums1And2.begin()));

    // create a set of the numbers that are in nums1 and nums3
    set<int> nums1And3;
    set_intersection(nums1Set.begin(), nums1Set.end(), nums3Set.begin(), nums3Set.end(), inserter(nums1And3, nums1And3.begin()));

    // create a set of the numbers that are in nums2 and nums3
    set<int> nums2And3;
    set_intersection(nums2Set.begin(), nums2Set.end(), nums3Set.begin(), nums3Set.end(), inserter(nums2And3, nums2And3.begin()));

    // add all 3 sets together
    set<int> nums1And2And3;
    set_union(nums1And2.begin(), nums1And2.end(), nums1And3.begin(), nums1And3.end(), inserter(nums1And2And3, nums1And2And3.begin()));
    set_union(nums1And2And3.begin(), nums1And2And3.end(), nums2And3.begin(), nums2And3.end(), inserter(nums1And2And3, nums1And2And3.begin()));

    // convert the set to a vector
    vector<int> nums1And2And3Vec(nums1And2And3.begin(), nums1And2And3.end());

    return nums1And2And3Vec;
}