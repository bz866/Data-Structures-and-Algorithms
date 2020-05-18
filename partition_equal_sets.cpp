/* 

LC 698. Partition to K Equal Sum Subsets

Note: 

1. Backtrack

*/

class Solution {
public:
	bool canPartitionSubsets(vector<int>& nums, int k) {
		if (k == 1) return true;

		int sum = accumulate(nums.begin(), nums.end(), 0);
		if (sum % k != 0) return false;
		int target = sum / k;
		sort(nums.begin(), nums.end());
		sort(nums.begin(), nums.end(), 
			[](const int& a, const int& b) {
				return a > b;
			});
		int beginIdx = 0;
		while (nums[beginIdx] == target) {
			++beginIdx;
			--k;
		}

		vector<int> subsums (k, 0);
		return search(nums, subsums, beginIdx, target);
	}

	bool search(const vector<int>& nums, vector<int>& subsums, int idx, const int& target) {
		if (idx == nums.size()) return true;

		int n = nums[idx];
		for (int& sub : subsums) {
			sub += n;
			if ( sub <= target && search(nums, subsums, idx+1, target) ) {
				return true;
			}
			sub -= n;
		}

		return false;
	}
};






