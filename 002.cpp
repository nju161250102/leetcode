using namespace std; 
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    int d = 0;
    ListNode* head = NULL;
    ListNode* p = NULL;
    while(1) {
        int sum = 0;
        if (l1 != NULL && l2 != NULL) {
            sum = l1->val + l2->val + d;
            l1 = l1->next;
            l2 = l2->next;
        } else if (l1 != NULL && l2 == NULL) {
            sum = l1->val + d;
            l1 = l1->next;
        } else if (l1 == NULL && l2 != NULL) {
            sum = l2->val + d;
            l2 = l2->next;
        } else {
            if (d != 0) {
                sum = d;
            } else {
                return head;
            }
        }
        ListNode* node = new ListNode(sum % 10);
        d = sum / 10;
        if (p == NULL) {
            p = node;
            head = node;
        }
        else p->next = node;
        p = node;
    }
}
