
// The implementation of the insertion-sort in Java

// Author: Eric Zeng


/**
 * Insertion sort of an array of characters into non-decreasing order 
 */
public static void insertionSort( char[] c )
{
	int n = c.length; // string length 

	for ( int i = 1; i < n; i++ ) // starting from the second character in a current character to be inserted
	{
		char curChar = c[i];
		int j = i - 1; // comparing with the left
		while ( ( j >= 0 ) && ( a[j] > curChar) )
		{
			c[ j + 1 ] == c [ j-- ];
		}
		a[ j + 1 ] = curChar;
	}
}