/*
	Two-D array coordinate as 1d coordinate
*/

unordered_set<string> seen; 
for (int i = 0; i < rowSize; ++i) {
	for ( int j = 0; j < colSize; ++j ) {
		idx = i * colSize + j;
		seen.insert(idx); // 1d coordinates in hashset easy to look up
	}
}

// -> convert back
int x = idx / colSize
int y = idx % colSize



/*


*/

`