#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<int> preorderTraversal(TreeNode* root) {
    //visit root, visit left, visit right
    vector<int> result;
    traverse(root, result);
    return result;
}

void traverse(TreeNode* root, vector<int>& result) {
    if (root == nullptr) {
        return;
    }
    result.push_back(root->val); //visit root
    traverse(root->left, result); //visit left
    traverse(root->right, result); //visit right
}