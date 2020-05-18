/*

LC 
109. Convert Sorted List to Binary Search Tree
108. Convert Sorted Array to Binary Search Tree

Note:
1. access the mid point
2. index or fast/slow pointers

*/

// 109. Convert Sorted List to Binary Search Tree
// fast slow pointers
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) return NULL;
        return sortedListToBST(head, NULL);
    }
    
    TreeNode* sortedListToBST(ListNode* head, ListNode* tail) {
        if (head == tail) return NULL;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != tail && fast->next->next != tail) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        TreeNode* root = new TreeNode(slow->val);
        root->left = sortedListToBST(head, slow);
        root->right = sortedListToBST(slow->next, tail);
        
        return root;
    }
};

// 108. Convert Sorted Array to Binary Search Tree
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size()-1);
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums, int left, int right) {
        if (left > right) return NULL;
        // int mid = left + (right - left) / 2;
        int mid = (right + left) / 2;
        
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = sortedArrayToBST(nums, left, mid-1);
        root->right = sortedArrayToBST(nums, mid+1, right);
        
        return root;
    }
};