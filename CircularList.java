package QuestionOne;

import java.util.AbstractList;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.lang.Math;
import java.util.Random;
import java.util.Collections;
import java.util.Iterator;


public class CircularList<T> extends AbstractList {
	
	private int capacity; // The max capacity of the circular list
	private int size; // Current number of elements in the circular list
	private int headIdx; // The index of the current front 
	private int tailIdx; // The index of the current tail
	private ArrayList<T> theValues; // Storage of contents, ArrayList with capacity length
	private Random randomizer = new Random(); // the randomizer for sampling
	
	// Constructor
	public CircularList(int newCapacity)
	{
		// Check invalid capacity value
		if (capacity < 0)
		{
			throw new IllegalArgumentException("Size n must greater than 0.");
		}
		
		this.capacity = newCapacity; // initialize the max capacity of the circular list
		this.theValues = new ArrayList<T> ( Collections.nCopies( this.capacity, (T) null ) ); // fixed length generic array list for storage; Note(1)
		this.size = 0; // Initialize as an empty circular list
		this.headIdx = 0; // The head of the circular list start from 0
		this.tailIdx = 0; // The tail of the circular list initialized as the last location
	} // testCircularList
	
	/**
	 * Get the capacity of the circular list
	 * @return
	 * 	int; the capacity 
	 */	
	public int capacity()
	{ 
		return this.capacity; 
	} // testCapacity
	
	/**
	 * Re-assign the capacity of the circular list
	 * @param newCapacity
	 */
	public void capacity(int newCapacity)
	{ 
		if (newCapacity < this.size())
		{
			throw new IllegalArgumentException("New capacity " + this.capacity + " is smaller than the number of item " + this.size + " in the original circular array");
		}
		if ( newCapacity <= 0 )
		{
			throw new IllegalArgumentException("New capacity should be larger than zero");
		}

		// immigrate all items to the array of the new capacity
		migrateToNewCapacityArrayList(newCapacity);
	} // testCapacityInt
	
	/**
	 * Get the size/number of elements in the circular list
	 */
	public int size()
	{
		return this.size; 
	} // testSize
	
	/**
	 * return a boolean to show if the array is empty
	 */
	public boolean isEmpty()
	{
		return this.size == 0; 
	} // testIsEmpty
	
	// remove all elements in the circular list
	public void clear()
	{
//		this.theValues = (T[]) new Object[capacity]; // making all values null, the garbage collector takes care of original values
		this.theValues = new ArrayList<T> ( Collections.nCopies( this.capacity, (T) null ) ); // all items as null
		this.headIdx = 0;
		this.tailIdx = 0;
		this.size = 0;
	} // testClear
	
	/**
	 * Get an item by index 
	 * @param virtualIdx: int; the index for the interface
	 * @return
	 * 	The item in the circular list <T>
	 */
	public T get( int virtualIdx )
	{
		checkNotEmpty();
		
		int physicalIdx = convertToPhysicalIdx( virtualIdx );
		return this.theValues.get( physicalIdx );
	} // testGetInt
	
	/**
	 * Get the item at the head
	 * @return
	 * 	generic item
	 */
	public T getFirst()
	{
		return this.theValues.get( this.headIdx );
	} // testGetFirst
	
	/**
	 * Get the item at the tail
	 * @return
	 * 	generic item
	 */
	public T getLast()
	{
		return this.theValues.get( this.tailIdx );
	} // testGetLast
	
	/**
	 * add an item to the head of the circular list
	 * @param item: generic type of element
	 */
	public void addFirst(T item)
	{
		if ( checkIsFull() )
		{
			grow(); // grow to double capacity if the array is full
		}
		if ( !isEmpty() )
		{
			this.headIdx--;
			this.headIdx = convertToPhysicalIdx( 0 );
		}
		this.theValues.set( this.headIdx, item ); // add the new item to one location ahead of the old head
		this.size++;
	} // testAddFirst
	
	/**
	 * add an item to the tail of the circular list
	 * @param item: generic type of element
	 */
	public void addLast(T item)
	{
		if ( checkIsFull() )
		{
			grow(); // grow to double capacity if the array is full
		}
		if ( !isEmpty() )
		{
			this.tailIdx++;
			this.tailIdx = convertToPhysicalIdx( this.size );
		}
		this.theValues.set( this.tailIdx, item ); // add the new item to one location after of the old tail
		this.size++;
	} // testAddLast
	
	/**
	 * Remove the item at the head of the circular list & return the removed item
	 * @return
	 * 	a generic item
	 */
	public T removeFirst()
	{
		checkNotEmpty();

		// remove and get the old item at head
		T itemRemoved = this.theValues.set( headIdx, null );
		this.size--;
		// reset the head index 
		if ( !isEmpty() ) // more than one item
		{
			this.headIdx++; // head reference move forward 
			this.headIdx = convertToPhysicalIdx( 0 ); // head index always have virtual index as 0; 
		}
		
		return itemRemoved;
	} // testRemoveFirst
	
	/**
	 * Remove the item at the tail of the circular list & return the removed item
	 * @return
	 * 	a generic item
	 */
	public T removeLast()
	{
		checkNotEmpty();
		
		// remove and get the old item at tail
		T itemRemoved = this.theValues.set( tailIdx, null );
		this.size--;
		// reset the tail index
		if ( !isEmpty() ) // more than one item
		{
			this.tailIdx--; // tail reference move backward
			this.tailIdx = convertToPhysicalIdx( Math.max( 0, this.size - 1 ) ); // tail index always have virtual index as this.size-1 or 0 
		}

		return itemRemoved;
	} // testRemoveLast
	
	/**
	 * Uniformly sample an item from the circular list
	 * @return
	 */
	public T sampleUniform()
	{
		checkNotEmpty();
		
		// sample an virtual index
		int virtualIdxSample = this.randomizer.nextInt( this.size - 1 ); // sampling, [min = 0, max= this.size - 1]
		// use the sample virtual index to get the sample item
		T itemSample = this.get( virtualIdxSample ); // get the sample item by the sample virtual index
		
		return itemSample;
	} // testSampleUniform
	
	/**
	 * if the current capacity is not enough for the new item; extend the circular list by doubling its capacity
	 */
	private void grow()
	{
		int doubleCapacity = 2 * this.capacity; // double the size 
		migrateToNewCapacityArrayList(doubleCapacity); // migrate original items to the new array list
	}
	
	/**
	 * Change the size of the circular list given new capacity, initialize a new array list, then migrate all
	 * original items to the new array list
	 * @param newCapacity: int; the new capacity of the circular list
	 */
	private void migrateToNewCapacityArrayList(int newCapacity)
	{
		ArrayList<T> newtheValues = new ArrayList<T> ( Collections.nCopies( newCapacity, (T) null ) ); // copy the old array list with all items
		int newSize = 0;
		int newtailIdx = 0;
		// copy all old items to the new array list
		for ( int virtualIdx = 0; virtualIdx < this.size; virtualIdx++ ) // copy all old items to the new array list
		{
			int physicalIdx = convertToPhysicalIdx( virtualIdx ); // virtual index for the new array list, physical index for the old arra list
			T item = this.theValues.get( physicalIdx );
			newtheValues.set( virtualIdx, item ); // migrate items one by one
			newSize++;
			newtailIdx++;
		}
		// re-initialize the circular array with new capacity
		this.capacity = newCapacity;
		this.theValues = newtheValues; // items migration done; garbage collection will erase the old array list
		this.size = newSize;
		this.headIdx = 0;
		this.tailIdx = newtailIdx;
	}
	
	/**
	 * The method convert interface virtual index to physical index of the circular array
	 * The interface take the virtual index that virtual head index is always the 0, and the virtual tail
	 * index is always the number of items(size) of the circular array
	 * @param virtualIdx: int; the virtual index for the interface
	 * @return
	 * 	physicalIdx: int; the actual index for the private array list
	 */
	private int convertToPhysicalIdx(int virtualIdx)
	{
		// virtual index must be an integer in [0, this.size-1]
		checkIndexRange(virtualIdx);
		
		int physicalIdx = ( virtualIdx + this.headIdx + this.capacity ) % this.capacity; // convert the virtual index to the physical index
		return physicalIdx;
	}
	
	/**
	 * check if the index is in [0, this.size-1]
	 * @param Idx: int; the index to be checked
	 * @return	
	 * 	e Exception || valid index
	 */
	private boolean checkIndexRange(int Idx)
	{
		if (Idx > this.size()) // out of range, raise exception
		{
			throw new IllegalArgumentException("The index should be an integer in "
					+ "[" + 0 + ", " + (this.size-1) + "]");
		}
		return true;
	}
	
	/**
	 * check if the array is empty, raise exception if true
	 * @return
	 * 	e Exception || not empty
	 */
	private boolean checkNotEmpty()
	{
		if ( this.isEmpty() )
		{
			throw new NoSuchElementException("Empty circular list");
		}
		return false;
	}
	
	/**
	 * if the array if full
	 * @return
	 *  boolean
	 */
	private boolean checkIsFull()
	{
		return this.size == this.capacity;
	}
}


//Personal Notes:
/*
1. Arrays is not generic. It is checked in both the compile time and the runtime. Arrays 
store the information of both the component and its type. During the runtime, we are not 
sure what the <T> is, so we must know the component type when we create the Array

2. 
*/