/*

1122. Relative Sort Array


Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

*/


class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> arr2Map;
        for (int i = 0; i < arr2.size(); ++i) {
            arr2Map[arr2[i]] = i;
        }
        
        auto arr2Order = [&](int a, int b) {
            if (arr2Map.count(a) && arr2Map.count(b)) return arr2Map[a] < arr2Map[b];
            else if (arr2Map.count(a)) return true;
            else if (arr2Map.count(b)) return false;
            else {
                return a < b;
            }
        };
        sort(arr1.begin(), arr1.end(), arr2Order);
        return arr1;
    }
};