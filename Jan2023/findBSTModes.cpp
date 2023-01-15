#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<int> findMode(TreeNode* root) {
    //make a map of the frequency of each element
    unordered_map<int, int> freq;
    inOrderTraverse(root, freq);
    
    //find the max frequency
    int maxFreq = 0;
    for (auto it = freq.begin(); it != freq.end(); it++) {
        if (it->second > maxFreq) maxFreq = it->second;
    }
    
    //find all the elements with the max frequency
    vector<int> res;
    for (auto it = freq.begin(); it != freq.end(); it++) {
        if (it->second == maxFreq) res.push_back(it->first);
    }
    
    return res;
}

void inOrderTraverse(TreeNode* root, unordered_map<int, int>& freq) {
    if (root == nullptr) return;
    inOrderTraverse(root->left, freq);
    freq[root->val]++;
    inOrderTraverse(root->right, freq);
}