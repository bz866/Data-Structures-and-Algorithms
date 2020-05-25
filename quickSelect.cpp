#include <iostream>
#include <vector>

using namespace std;

// int partition(vector<int>& arr, int left, int right) {
// 	int i = left - 1;
// 	int pivot = arr[right];

// 	for (int j = left; j < right; ++j) {
// 		if (arr[j] < pivot) {
// 			++i;
// 			swap(arr[i], arr[j]);
// 		}
// 	}

// 	swap(arr[i+1], arr[right]);
// 	return i+1;
// }

int partition(vector<int>& arr, int left, int right) {
	int pivot = arr[right];
	int start = left;
	int end = right - 1;

	while (start <= end) {
		if (arr[start] < pivot) {
			++start;
		}
		else if (arr[end] >= pivot) {
			--end;
		}
		else {
			swap(arr[start], arr[end]);
			++start;
			--end;
		}
	}

	swap(arr[start], arr[right]);
	return start;
}


void quickSelect(vector<int>& arr, int left, int right, int target) {
	if (left >= right) return;

	int pi = partition(arr, left, right);
	if (pi < target) {
		quickSelect(arr, pi+1, right, target);
	}
	else if (pi > target) {
		quickSelect(arr, left, pi-1, target);
	}
	else return;

	return;
}

vector<int> getTopK(vector<int>& arr, int K) {
	if (arr.empty() || K == 0) return vector<int> ();
	quickSelect(arr, 0, arr.size()-1, K-1);
	for (int n : arr) cout << n << " ";
	cout <<endl;
	return vector<int> (arr.begin(), arr.begin()+K);
}

int main(int argc, char const *argv[])
{
	int values[] = {21,3,34,5,13,8,2,55,1,19};
	vector<int> arr (values, values + 10);
	int K = 4;

	vector<int> res = getTopK(arr, K);
	for (int n : res) cout << n << " ";
	cout <<endl;
	return 0;
}