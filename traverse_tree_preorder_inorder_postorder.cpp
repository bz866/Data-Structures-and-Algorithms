/*

LC
144. Binary Tree Preorder Traversal
94. Binary Tree Inorder Traversal
145. Binary Tree Postorder Traversal

*/

// preorder
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        // [1,2,3,4,5,6,7]
        //    4 
        //  3   6
        // 1 2 5 7
        // 4 3 1 2 6 5 7
        //
        if (!root) return {};
        
        vector<int> res;
        stack<TreeNode*> stk;
        stk.push(root);
        while (stk.size() > 0) {
            TreeNode* node = stk.top(); stk.pop();
            res.push_back(node->val);
            if (node->right) stk.push(node->right);
            if (node->left) stk.push(node->left);
        }
        
        return res;
    }
};

// inorder // right first, need reverse at the end
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        // [1,2,3,4,5,6,7]
        //    4 
        //  3   6
        // 1 2 5 7
        // 1 3 2 4 5 6 7
        //
        vector<int> res;
        stack<TreeNode*> stk;
        TreeNode* node = root;
        while (stk.size() > 0 || node) {
            while (node) {
                stk.push(node);
                node = node->right;
            }        
            
            node = stk.top(); stk.pop();
            res.push_back(node->val);
            node = node->left;
        }

        return vector<int> (res.rbegin(), res.rend());
    
    }
};

// inorder, left first, no need to reverse at the last
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        stack<TreeNode*> stk;
        TreeNode* node = root;
        while (node || stk.size() > 0) {
            while (node) {
                stk.push(node);
                node = node->left;
            }
            node = stk.top(); stk.pop();
            res.push_back(node->val);
            node = node->right;
        }

        return res;
    }
};

// postorder
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        // [1,2,3,4,5,6,7]
        //    4 
        //  3   6
        // 1 2 5 7
        // 1 2 3 5 7 6 4
        //
        if (!root) return {};
        
        vector<int> res;
        stack<TreeNode*> stk;
        stk.push(root);
        while (stk.size() > 0) {
            TreeNode* node = stk.top(); stk.pop();
            res.push_back(node->val);
            if (node->left) stk.push(node->left);
            if (node->right) stk.push(node->right);
        }
        
        return vector<int> (res.rbegin(), res.rend());
    }  
};



