/* 

Binary Search

Brief:
Binary search is efficient for using the fact that the array is inorder. 
After each round of searching, we can narrow down the range to half of the previous round. 
Keep narrowing down till it becomes one number. 

Note: Boundary case Handling
278, 852
- Return right for its stationarity
- Use (left < right)

Note:
35
left right end location
left > target
right <= target
Ends like, left right switch the position

val, val, val, val, val, val

	  ^.   ^. 
	right, left

162
right pointer is still stable

*/ 


// Template
// Better for FIND TARGET
int binarySearch(vector<int>& nums, int target) {
	int left = 0;
	int right = nums.size() - 1;

	while (left <= right) {
		int mid = left + (right - left) / 2;
		if (nums[mid] < target) {
			left = mid + 1;
		}
		else if (nums[mid] > target) {
			right = mid - 1;
		}
		else return mid;
	} 

	return -1; // not found
}

// Better for 
// 1. target exists for sure
// 2. decide how to expand the interval and certify the location
int binarySearch(vector<int>& nums, int target) {
	int left = 0;
	int right = nums.size() - 1;

	while (left <= right) {
		int mid = left + (right - left) / 2;
		if (nums[mid] < left) { // only 2 if - else
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}

	return right; // return right not mid 
}

// 278 First Bad Version 
class Solution {
public:
	int firstBadVersion(int n) {
		int left = 1;
		int right = n;
		while (left < right) { // use left < right to make right land on the target
			int mid = left + (right - left) / 2;
			if (isBadVersion(mid)) right = mid; // left and right end at the same location
			else left = mid + 1;
		}

		return right;
	}
};

// 852 Peak Index in a Mountain Array
class Solution {
public:
	int peakIndexInMountainArray(vector<int>& A) {
		int left = 0;
		int right = A.size() - 1;
		while (left < right) { // make sure right always on the right of left, so mid+1 always exist
			int mid = left + (right - left) / 2;
			if (A[mid] < A[mid+1]) left = mid + 1;
			else right = mid;
		}
		return right;
	}
};

// 35 Search Insert Position
class Solution {
public: 
	int searchInsert(vector<int>& nums, int target) {
		int left = 0;
		int right = nums.size() - 1;
		while (left <= right) {
			int mid = left + (right - left) / 2;
			if (nums[mid] < target) left = mid + 1;
			else right = mid - 1;
		}

		return right + 1;
	}
};

// 162 Find Peak Element
class Solution {
public:
	int findPeakElement(vector<int>& nums) {
		int left = 0;
		int right = nums.size() - 1;
		while (left < right) {
			int mid = left + (right - left) / 2;
			if (nums[mid] > nums[mid+1]) right = mid;
			else left = mid + 1;
		}

		return right;
	}
};








