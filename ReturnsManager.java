package QuestionTwo;

import QuestionOne.CircularList;
import java.util.ArrayList;
import java.util.TreeMap;
import java.util.SortedMap;
import java.util.Collections;
import java.util.Map;
import java.util.NoSuchElementException;
import java.lang.Math;

public class ReturnsManager {
	
	private int qSize; // the length of the queue
	private CircularList queueReturns; // use the CircularList to implement the queue features, FIFO
	private TreeMap<String, Integer> treeReturns; // use a treemap to sort all returns in O(nlogn);
	// Note: Use the string of a double as key for fast comparing, Value as the count of the times of duplicates of a return
	
	// Constructor
	public ReturnsManager ( int newSize)
	{
		this.qSize = newSize;
		// the cnt returns will never be larger than qSize so that the queue never grows to save space in memory 
		this.queueReturns = new CircularList( this.qSize ); 
		this.treeReturns = new TreeMap<String, Integer> ();
	} // testReturnsManager
	
	/**
	 * Add returns to ReturnsManager, if the queue is full, remove the earliest return
	 * @param newReturn
	 */
	public void add (double newReturn ) // O(logn) + O(1)
	{
		String newReturnStr = String.valueOf(newReturn);
		if (this.queueReturns.size() == this.queueReturns.capacity())
		{
			double item = (Double) this.queueReturns.removeFirst(); // FIFO, remove the earliest return O(1)
			treeMapRemoveOccurrence( treeReturns.firstKey()); // O(logn)
		}
		// add the most recent return
		this.queueReturns.addLast( newReturn ); // append the new return, FIFO O(1)
		treeMapAddOccurence( newReturnStr); // O(logn)
	} // testAdd
	
	/**
	 * Get the most recent return
	 * @return
	 * 	double; the latest return
	 */
	public double getLast()
	{
		checkNotEmpty();
		
		return (Double) this.queueReturns.getLast(); // the latest return is at the end of the queue
	}
	
	/**
	 * Get numReturns of returns that are less than or equal to the given referenceReturn
	 * @param referenceReturn: double; the reference return that should be greater than or equal to
	 * @param numReturns: int; number of returns required
	 * @return
	 * 	ArrayList<Double> a list of returns 
	 */
	public ArrayList<Double> getLower( double referenceReturn, int numReturns)
	{
		ArrayList<Double> returnsArr = new ArrayList<Double> (numReturns);
		String referenceReturnStr = String.valueOf(referenceReturn);
//		TreeMap<String, Integer> tempTree = this.treeReturns.clone();
		
		// Get entries with keys that smaller or equal to the reference return
		// Get mappings of returns that is strictly smaller than the referenceReturn till enough
		int cnt = 0;
		while (cnt < numReturns)
		{
			Map.Entry<String, Integer> lowerReturnEntry;
			lowerReturnEntry = this.treeReturns.lowerEntry(referenceReturnStr); // O(logn) // get lower return mapping
			if ( lowerReturnEntry == null ) // not enough lower return exists
			{
				break;
			}
			treeMapRemoveOccurrence( lowerReturnEntry.getKey() ); // Amortize O(logn) // deduct the occurrence
			double lowerReturn = Double.valueOf( lowerReturnEntry.getKey() );
			returnsArr.add( lowerReturn ); // append to the result list
			cnt++;
		}
		// get mappings of returns that is equal to the referenceReturn, if not enough  
		if ( this.treeReturns.containsKey( referenceReturnStr ) && cnt < numReturns )
		{
			double lowerReturn;
			lowerReturn = Double.valueOf( referenceReturnStr );
			treeMapRemoveOccurrence( referenceReturnStr ); // deduct the occurrence
			returnsArr.add(lowerReturn); // append to the result list
			cnt++;
		}
		
		return returnsArr;
	}
	
	/**
	 * Get numReturns of returns that are greater than or equal to the given referenceReturn
	 * @param referenceReturn: double; the reference return that should be greater than or equal to
	 * @param numReturns: int; number of returns required
	 * @return
	 * 	ArrayList<Double> a list of returns 
	 */
	public ArrayList<Double> getHigher( double referenceReturn, int numReturns)
	{
		ArrayList<Double> returnsArr = new ArrayList<Double> (numReturns);
		String referenceReturnStr = String.valueOf( referenceReturn );
		
		// Get entries with keys that larger or equal to the reference return
		// Get mappings of returns that is strictly larger than the referenceReturn till enough
		int cnt = 0;
		while ( cnt < numReturns )
		{
			Map.Entry<String, Integer> higherReturnEntry;
			higherReturnEntry = this.treeReturns.higherEntry( referenceReturnStr );  // O(logn) //get higher return mapping
			if ( higherReturnEntry == null ) // not enough higher return exists
			{
				break;
			}
			treeMapRemoveOccurrence( higherReturnEntry.getKey() ); // Amortize O(logn) // deduct the occurrence
			double highReturn = Double.valueOf( higherReturnEntry.getKey() );
			returnsArr.add( highReturn ); // append to the result list
			cnt++;
		}
		// get mappings of returns that is equal to the referenceReturn, if not enough 
		if ( this.treeReturns.containsKey( referenceReturnStr ) && cnt < numReturns )
		{
			double higherReturn;
			higherReturn = Double.valueOf( referenceReturnStr );
			treeMapRemoveOccurrence( referenceReturnStr ); // deduct the occurrence
			returnsArr.add( higherReturn );
			cnt++;
		}
		
		return returnsArr;

	}
	
	/**
	 * Update the occurrence of a return 
	 * If return exists in the queue/tree, occurrence += 1
	 * If new return appears, occurrence = 1
	 * @param treeMapIn: TreeMap<ReturnStr, OccurrenceInt>
	 * @param key: The string of the return to update
	 * @return
	 */
	private void treeMapAddOccurence(String key)
	{
		if ( this.treeReturns.containsKey(key) ) // existed return appearance
		{
			int newCnt = this.treeReturns.get(key) + 1; // accumulate the count of occurrence
			this.treeReturns.put( key, newCnt);
		}
		else // new return appearance
		{
			this.treeReturns.put( key, 1 ); 
		}
	}
	
	/**
	 * Update the occurrence of a return 
	 * If return exists in the queue/tree, occurrence -= 1
	 * If new return appears, occurrence = 1
	 * @param treeMapIn: TreeMap<ReturnStr, OccurrenceInt>
	 * @param key: The string of the return to update
	 * @return
	 */
	private void treeMapRemoveOccurrence(String key)
	{	
		if ( this.treeReturns.get( key ) >= 2 ) // the return appears more than once
		{
			int newCnt = this.treeReturns.get( key ) - 1; // deduct one occurrence
			this.treeReturns.put(key, newCnt);
		}
		else // the return only appeared once
		{
			this.treeReturns.remove( key ); // remove
		}
	}
	
	/**
	 * Check the queue of the ReturnsManager is empty
	 * @return
	 */
	private boolean checkNotEmpty()
	{
		if ( this.queueReturns.size() == 0)
		{
			throw new NoSuchElementException("Queue of the ReturnsManager is Empty");
		}
		return true;
	}
}
	
	
