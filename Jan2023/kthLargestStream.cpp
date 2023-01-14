#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class KthLargest {
public:
    //make a min heap
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
    KthLargest(int k, vector<int>& nums) {
        //set k
        this->k = k;

        //add all elements to pq
        for (int i = 0; i < nums.size(); i++) {
            pq.push(nums[i]);
        }

        //pop until pq.size() == k
        while (pq.size() > k) {
            pq.pop();
        }
    }
    
    int add(int val) {
        //add val to pq and pop smallest element
        //return the min element in the heap
        pq.push(val);
        if (pq.size() > k) pq.pop();
        return pq.top();
    }
};

int main() {
    vector<int> nums = {4,5,8,2};
    KthLargest* obj = new KthLargest(3, nums);
    int param_1 = obj->add(3);
    cout << param_1 << endl;
    int param_2 = obj->add(5);
    cout << param_2 << endl;
    int param_3 = obj->add(10);
    cout << param_3 << endl;
    int param_4 = obj->add(9);
    cout << param_4 << endl;
    int param_5 = obj->add(4);
    cout << param_5 << endl;
    return 0;
}