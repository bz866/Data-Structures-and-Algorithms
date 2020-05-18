/*

Limit the low and high search boundary
Maximum search 32 times for 32-bit system 2 ** 32 = 2,147,483,647

Then check if answer valid, change the search range to narrow down to the target answer

*/

class Solution{
public:
	int shipWithinDays(vector<int>& weights, int D) {
		int low = INT_MAX;
		int high = 0;
		// bound the search range 
		// lower as the smallest load
		// higher as the sum of all weights
		for (int w : weights) {
			low = min(low, w);
			high += w;
		} 

		// binary search within the range
		while (low < high) {
			int cap = low + (high - low) / 2; // keep guessing
			// narrow down search range based on search condition
			if (validSolution(weights, cap, D)) high = cap; 
			else low = cap + 1;
		}

		return high;
	}

	bool validSolution(vector<int>& weights, int cap, int D) {
		int days = 0;
		for (int i = 0; i < weights.size();) {
			int dayWeight = 0;
			int j = i;
        
			while (j < weights.size() && dayWeight + weights[j] <= cap) {
				dayWeight += weights[j];
				++j;
			}
			++days;
			if (days > D) return false;
			i = j;
		}

		return true;
	}
};
