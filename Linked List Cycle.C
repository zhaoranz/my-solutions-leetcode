/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if (head == NULL || head -> next ==NULL){
        return false;
    }
    struct ListNode * i = head;
    struct ListNode * j = head -> next;
    while (i != j ){
        if (j == NULL || j->next == NULL){
            return false;
        }
        i = i -> next;
        j = j -> next -> next;
    }
    return true;
    
    
}
