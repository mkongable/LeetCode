#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr) {
        return head;
    } else {
        ListNode* curr = head;
        while (curr != nullptr) {
            if (curr->next != nullptr && curr->val == curr->next->val) {
                curr->next = curr->next->next; //remove intermediate node
                continue;
            } else {
                curr = curr->next;
            }
        }
    }
    return head;
}

int main() {
    ListNode* head = new ListNode(1);
    return 0;
}