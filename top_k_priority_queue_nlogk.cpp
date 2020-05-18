/*

Top K problem

Note:
1. priority_queue
2. self-defined comparator in C++
3. logorithm insert and remove in heap

*/


class Solution {
private:
    typedef pair<string, int> Node;
    // typedef function<bool(const Node&, const Node&)> Compare;
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> count;
        for (const string& w : words) {
            ++count[w];
        }
        
        // self defined comparator using lambda 
        auto comp = [](const Node& na, const Node& nb) {
            if (na.second == nb.second) return na.first < nb.first;
            return na.second > nb.second;
        }; 
        
        // priority queue with self defined comparator
        priority_queue<Node, vector<Node>, decltype(comp)> minHeap(comp);
        
        for (const auto& p : count) {
            minHeap.push(p);
            if (minHeap.size() > k) minHeap.pop();
        }
        
        vector<string> res;
        
        while( !minHeap.empty() ){
            res.push_back(minHeap.top().first);
            minHeap.pop();
        }
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};
