#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int maxHeight(TreeNode* root) {
    if (root == nullptr) return 0;
    return max(maxHeight(root->left), maxHeight(root->right)) + 1;
}

bool isBalanced(TreeNode* root) {
    int maxHL = maxHeight(root->left);
    int maxHR = maxHeight(root->right);
    if (abs(maxHL - maxHR) > 1) return false;
    return true;
}