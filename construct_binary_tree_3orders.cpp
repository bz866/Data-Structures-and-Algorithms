/* 

LC 
- 1008 Construct Binary Search Tree from Preorder Traversal   
- 105 Construct Binary Tree from Preorder and Inorder Traversal    
- 106 Construct Binary Tree from Inorder and Postorder Traversal
- 889. Construct Binary Tree from Preorder and Postorder Traversal

Note:
1. Index problems 
2. head of preorder and tail of postorder are always roots
3. inorder helps to split to left and right

*/

// 889. Construct Binary Tree from Preorder and Postorder Traversal
class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        if (pre.size() == 0 || post.size() == 0) return NULL;
        return constructFromPrePost(pre, 0, pre.size()-1, post, 0, post.size()-1);
    }
    
    TreeNode* constructFromPrePost(vector<int>& pre, int preleft, int preright, vector<int>& post, int postleft, int postright) {
        if (preleft > preright || postleft > postright) return NULL;
        // if (preleft == preright && postleft == postright) return new TreeNode(pre[preleft]);
        if (preleft == preright) return new TreeNode(pre[preleft]);
        
        int idx = -1;
        for (idx = postleft; idx <= postright; ++idx) {
            if (pre[preleft+1] == post[idx]) break;
        }
        
        TreeNode* root = new TreeNode(pre[preleft]);
        root->left = constructFromPrePost(pre, preleft+1, preleft + idx - postleft + 1, post, postleft, idx);
        root->right = constructFromPrePost(pre, preleft + 1 + (idx - postleft) + 1, preright, post, idx+1, postright-1);
        
        return root;
    }
};

// 106 Construct Binary Tree from Inorder and Postorder Traversal
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTree(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
    
    TreeNode* buildTree(vector<int>& inorder, int ileft, int iright, vector<int>& postorder, int pleft, int pright) {
        if (ileft > iright || pleft > pright) return NULL;
        int i = -1;
        for (i = ileft; i <= iright; ++i) {
            if (postorder[pright] == inorder[i]) break;
        }
        
        TreeNode* root = new TreeNode(postorder[pright]);
        root->left = buildTree(inorder, ileft, i-1, postorder, pleft, pleft + i - ileft - 1);
        root->right = buildTree(inorder, i+1, iright, postorder, pleft + i - ileft, pright-1);
            
        return root;
    }
};

// 105 Construct Binary Tree from Preorder and Inorder Traversal    
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildTree(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
    }
    
    TreeNode* buildTree(vector<int>& preorder, int pleft, int pright, vector<int>& inorder, int ileft, int iright) {
        if (pleft > pright || ileft > iright) return NULL;
        int i;
        for (i = ileft; i <= iright; ++i) {
            if (inorder[i] == preorder[pleft]) break;
        }
        TreeNode* root = new TreeNode(preorder[pleft]);
        root->left = buildTree(preorder, pleft+1, pleft + i - ileft, inorder, ileft, i-1);
        root->right = buildTree(preorder, pleft + i - ileft + 1, pright, inorder, i+1, iright);
            
        return root;
    }
};

// 1008 Construct Binary Search Tree from Preorder Traversal   
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode* dummy = new TreeNode(INT_MAX);
        for (int n : preorder) {
            insert(n, dummy);
        }
        
        return dummy;
    }
    
    void insert(int n, TreeNode* node) {
        if (node->val == INT_MAX) {
            node->val = n;
            return;
        }
        
        if (n > node->val) {
            if (!node->right) node->right = new TreeNode(n);
            else insert(n, node->right);
        }
        else if (n < node->val) {
            if (!node->left) node->left = new TreeNode(n);
            else insert(n, node->left);
        }
        
        return;
    }
};