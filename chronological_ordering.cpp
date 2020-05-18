/*

253. Meeting Rooms II

Note: 
Two points and two sorted arrays for times of start and times of end

*/

class Solution {
public:
    int minMeetingRooms( vector<vector<int>>& intervals ) {
        if ( intervals.size() == 0 ) return 0;
        
        int ans = 0;
        vector<int> starts (intervals.size() );
        vector<int> ends (intervals.size() );
        for ( int i = 0; i < intervals.size();++i ) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        
        int startIdx = 0;
        int endIdx = 0;
        
        while ( startIdx < intervals.size() ) {
            if ( starts[startIdx] >= ends[endIdx] ) { // one meeting has ended, one extra meeting room to use
                --ans; // free one room
                ++endIdx; // next time that a meeting ends
            }
            // a new meeting starts, one extra room needed
            ++ans; 
            ++startIdx;
            
        }
        
        return ans;
    }
};
