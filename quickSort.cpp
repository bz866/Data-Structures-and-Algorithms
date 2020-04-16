#include <iostream>
#include <vector>

using namespace std;

void swap(int* a, int* b ) {
	int t = *(a);
	*(a) = *(b);
	*(b) = t;
};

int partition(vector<int>& arr, int left, int right) {
	int i = left - 1;
	int pivot = arr[right];

	for (int j = left; j < right; ++j) {
		if (arr[j] < pivot) { // < ascending, > descending
			i++;
			swap( &arr[i], &arr[j] );
		}
	}

	swap( &arr[i+1], &arr[right] );
	return i+1;
};

void quickSort(vector<int>& arr, int left, int right) {
	if ( left >= right ) return;

	int pi = partition( arr, left, right );
	quickSort( arr, left, pi-1 );
	quickSort( arr, pi+1, right );

	return;
};

int main(int argc, char const *argv[])
{
	
	vector<int> vec { 2,43,6,5,7,6,9,4,5,77,3,43,5,2,3 };

	quickSort(vec, 0, vec.size()-1);

	for (int n : vec) cout << n << " ";

	cout << endl;

	return 0;
}


