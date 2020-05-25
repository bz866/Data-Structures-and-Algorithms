/* 

Quick Sort: O(NlogN)
Quick Select - average O(N) - worse O(N^2)

973. K Closest Points to Origin

Note:
1. all built-in head are in natural order, 1,2,3,4,5,6,....


*/

// 973. K Closest Points to Origin
// Quick Selection

class Solution {
public:
	vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
		if (points.empty() || K == 0) return {};
		quickSelect(points, 0, points.size()-1, K-1);
		return vector<vector<int>> (points.begin(), points.begin() + K);
	}

	void quickSelect(vector<vector<int>>& points, int left, int right, int target) {
		if (left >= right) return;

		int pi = partition(points, left, right);
		if (pi < target) {
			quickSelect(points, pi+1, right, target);
		}
		else if (pi > target) {
			quickSelect(points, left, pi-1, target);
		}
		else return;

		return;
	}
 
	int partition(vector<vector<int>>& points, int left, int right) {
		int i = left - 1;
		vector<int>& pivot = points[right];

		for (int j = left; j < right; ++j) {
			if ( distance(points[j]) < distance(pivot) ) {
				++i;
				swap(points[i], points[j]);
			}
		}

		swap(points[i+1], points[right]);
		return i+1;
	}

	int distance(vector<int>& p) {
		return p[0] * p[0] + p[1] * p[1];
	}
};

// 973. K Closest Points to Origin
// Heapify
class Solution {
public: 
	vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
		if (points.empty() || K == 0) return {};

		auto distanceOrder = [](vector<int>& pa, vector<int>& pb) {
			if (pa[0]*pa[0]+pa[1]*pa[1] < pb[0]*pb[0]+pb[1]*pb[1]) return 1; // 1 go to the bottom
			else return 0;
		};

		priority_queue<vector<int>, vector<vector<int>>, decltype(distanceOrder)> maxHeap(distanceOrder);

		for (auto& p : points) {
			maxHeap.push(p);
			if (maxHeap.size() > K) maxHeap.pop();
		}

		vector<vector<int>> res;
		while ( !maxHeap.empty() ) {
			res.push_back(maxHeap.top());
			maxHeap.pop();
		}

		return res;
	}
};


