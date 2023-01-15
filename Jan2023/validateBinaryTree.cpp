#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool isValidBST(TreeNode* root) {
    vector<int> inOrderResult;
    inOrderTraverse(root, inOrderResult);

    //verify all the elements in inOrderResult are in ascending order
    int cur = inOrderResult[0];
    for (int i = 1; i < inOrderResult.size(); i++) {
        if (inOrderResult[i] <= cur) return false;
        cur = inOrderResult[i];
    }
    return true;
}

void inOrderTraverse(TreeNode* root, vector<int>& inOrderResult) {
    if (root == nullptr) return;
    inOrderTraverse(root->left, inOrderResult);
    inOrderResult.push_back(root->val);
    inOrderTraverse(root->right, inOrderResult);
}