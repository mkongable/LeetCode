#include <iostream>
#include <vector>
#include <algorithm>
#include <string>


using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (list1 == nullptr) {
        return list2;
    }
    if (list2 == nullptr) {
        return list1;
    }
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
    while (list1 != nullptr && list2 != nullptr) {
        if (list1->val < list2->val) {
            if (head == nullptr) {
                head = list1;
                tail = list1;
            } else {
                tail->next = list1;
                tail = tail->next;
            }
            list1 = list1->next;
        } else {
            if (head == nullptr) {
                head = list2;
                tail = list2;
            } else {
                tail->next = list2;
                tail = tail->next;
            }
            list2 = list2->next;
        }
    }
    if (list1 != nullptr) {
        tail->next = list1;
    }
    if (list2 != nullptr) {
        tail->next = list2;
    }
    return head;
}

int main() {
    ListNode* list1 = new ListNode(1);
    list1->next = new ListNode(2);
    list1->next->next = new ListNode(4);
    ListNode* list2 = new ListNode(1);
    list2->next = new ListNode(3);
    list2->next->next = new ListNode(4);
    ListNode* merged = mergeTwoLists(list1, list2);
    while (merged != nullptr) {
        cout << merged->val << " ";
        merged = merged->next;
    }
    cout << endl;
}