/*

Bucket sorting for topK

347. Top K Frequent Elements

Note:
1. bucket sort - a n size list to store elements with same frequency
2. iterate the bucket from the end to the begin to extrat elements with top K frequency 

*/ 



// bucket sort top K
// Since we know the frequency of each element is 1 <= freq <= n
// initialize a bucket with size n + 1
// count frequency
// put elements with same frequency into the same bucket
// iterate the bucket from its back
// till we find top K frequent elements
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        int maxFreq = 0;
        for (const int& n : nums) {
            maxFreq = max(maxFreq, ++count[n]);
        }
        
        unordered_map<int, vector<int>> bucket(maxFreq + 1);
        for (const pair<int,int>& p : count){
            bucket[p.second].push_back(p.first);
        }
        
        vector<int> res;
        for (int i = maxFreq; i > 0; --i) {
            auto item = bucket.find(i);
            if ( item == bucket.end() ) continue;
            res.insert(res.end(), item->second.begin(), item->second.end());
            if (res.size() >= k) break;
        }
        
        return res;
    }
};