#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    //make a priority queue
    priority_queue<int> pq;
    for (int i = 0; i < nums.size(); i++) {
        pq.push(nums[i]);
    }

    //take top k-1 elements out
    for (int i = 0; i < k-1; i++) {
        pq.pop();
    }

    return pq.top();
}