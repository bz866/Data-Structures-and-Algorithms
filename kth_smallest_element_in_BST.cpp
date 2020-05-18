/*

LC
230. Kth Smallest Element in a BST

Note:
1. BST characteristic, left < mid < right
2. stack go depth
3. always keep the latest smallest node as the top of the stack

*/ 


class Solution {
public:
	int kthSmallest(TreeNode* root, int k) {
		stack<TreeNode*> stk;
		TreeNode* node = root;
		while (node) {
			stk.push(node);
			node = node->left;
		}

		int i = 0;
		while (stk.size() > 0 && i < k) {
			node = stk.top(); stk.pop();
			++i;

			TreeNode* rightNode = node->right;
			while (rightNode) {
				stk.push(rightNode);
				rightNode = rightNode->left;
			}
		}

		return node->val;
	}
};