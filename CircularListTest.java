package QuestionOne;

import static org.junit.Assert.*;
import org.junit.Test;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.List;
import static org.junit.matchers.JUnitMatchers.hasItems;
import static java.lang.System.out;
import java.util.Iterator;



public class CircularListTest {
	
	@Test
	public void testCircularList() {
		CircularList testCircularList = new CircularList(5);
	}
	
	@Test
	public void testSize() {
		CircularList testCircularList = new CircularList(5);
		assertTrue(testCircularList.size() == 0);
	}

	@Test
	public void testIsEmpty() {
		CircularList testCircularList = new CircularList(5);
		assertTrue(testCircularList.isEmpty() == true);
	}

	@Test
	public void testClear() {
		
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");	
		testCircularList.clear();
		// empty Circular list
		assertTrue(testCircularList.capacity() == 5);
		assertTrue(testCircularList.size() == 0);
	}

	@Test
	public void testCapacity() {
		CircularList testCircularList = new CircularList(5);
		assertTrue(testCircularList.capacity() == 5);	
	}

	@Test
	public void testCapacityInt() {
		CircularList testCircularList = new CircularList(5);
		// 5
		assertTrue(testCircularList.capacity() == 5);
		testCircularList.capacity(7);
		// 7
		assertTrue(testCircularList.capacity() == 7);
		testCircularList.capacity(10);
		// 10
		assertTrue(testCircularList.capacity() == 10);
	}

	@Test
	public void testGetInt() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");	
		testCircularList.addLast("Second Item");
		testCircularList.addLast("Third Item");

		// [First, Second, Third, null, null]
		assertTrue(testCircularList.get(0) == "First Item");
		assertTrue(testCircularList.get(2) == "Third Item");
	}
	
	@Test
	public void testGetFirst()
	{
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("Second Item");	
		testCircularList.addFirst("First Item");
//		testCircularList.addLast("Third Item");
		// [First(head), Second(tail), null, null, null]
		assertTrue(testCircularList.getFirst() == "First Item");
	}
	
	@Test
	public void testGetLast()
	{
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");	
		testCircularList.addLast("Second Item");
		testCircularList.addLast("Third Item");
		// [First(head), Second, Third(tail), null, null]
		assertTrue(testCircularList.getLast() == "Third Item");
	}


	@Test
	public void testAddFirst() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");
		testCircularList.addFirst("First Item");
		testCircularList.addFirst("First Item");
		testCircularList.addFirst("First Item");
		testCircularList.addFirst("First Item");

		testCircularList.addFirst("New Item");

		// [New(head), First(tail), First, First, First]
		assertTrue(testCircularList.getFirst() == "New Item");

	}

	@Test
	public void testAddLast() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addLast("First Item");
		testCircularList.addLast("First Item");
		testCircularList.addLast("First Item");
		testCircularList.addLast("First Item");
		testCircularList.addLast("First Item");

		testCircularList.addLast("New Item");

		// [New(tail), First(head), First, First, First]
		assertTrue(testCircularList.getLast() == "New Item");

	}

	@Test
	public void testRemoveFirst() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");
		testCircularList.addLast("Last Item");
		testCircularList.removeFirst();

		assertTrue( testCircularList.get( 0 ) ==  "Last Item");
	}

	@Test
	public void testRemoveLast() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addFirst("First Item");
		testCircularList.addLast("Second Item");
		testCircularList.addLast("Last Item");
		testCircularList.removeLast();
		assertTrue( testCircularList.getLast() ==  "Second Item");
	}

	@Test
	public void testSampleUniform() {
		CircularList testCircularList = new CircularList(5);
		testCircularList.addLast("First Item");
		testCircularList.addLast("Second Item");

		// can only from one of the above two
		assertTrue( testCircularList.sampleUniform() == "First Item" ||
				testCircularList.sampleUniform() == "Second Item");
	}
	
//	@Test
//    @SuppressWarnings("unchecked")
//	// Use method.invoke to test the private method
//	public void testPrivateConvertToPhysicalIdx() throws Exception
//	{
//		// reference output as [5, 6(tail), null, 3(head), 4]
//		CircularList testCircularList = new CircularList(5);
//		for (int i = 0; i < 7; i++)
//		{
//			testCircularList.addLast( i );
//		}
//		testCircularList.removeLast();
//		
//		// output for testing
//		Method mthd = testCircularList.getClass().getDeclaredMethod( "convertToPhysicalIdx", int.class);	
//		mthd.setAccessible( true ); // required to use private methods
//		List<Integer> input = Arrays.asList( 3, 1 );
//		List<Integer> output = (List<Integer>) mthd.invoke( mthd, input ); // 1, 4
//		List<Integer> refOut = Arrays.asList( 1, 4 );  
//		out.format("%d -> %d", output, 1);
//		assertTrue( output.equals( refOut ) ); 
//	}
	
	@Test
	public void testMain() {
		int capacity = 5;
		CircularList<Integer> cl = new CircularList<Integer>( capacity );
		// Make sure circular list correctly circles underlying array
		for( int i = 0; i < 5; i++ )
		    cl.addLast( i );
		for( int i = 5; i < 10; i++ ) {
		    assertTrue( cl.removeFirst() == ( i - 5 ) );
		    cl.addLast( i );
		}
		// Empty list
		cl.clear();
		// Check size and capacity
		assertTrue( cl.size() == 0 );
		assertTrue( cl.capacity() == 5 );
		// 1
		cl.addLast( 7 );
		// Check get
		assertTrue( cl.get( 0 ) == 7 );
		// Check getFirst
		assertTrue( cl.getFirst() == 7 );
		// Check size
		assertTrue( cl.size() == 1 );
		// 2
		cl.addLast( 11 );
		// 3
		cl.addLast( 13 );
		// 4
		cl.addLast( 113 );
		assertTrue( cl.getLast() == 113 );
		// 5
		cl.addLast( 227 );
		assertTrue( cl.size() == 5 );
		// 4
		assertTrue( cl.removeFirst() == 7 );
		// 5
		cl.addFirst( 109 );
		// 6, grows to capacity 10
		cl.addLast( 53 );
		assertTrue( cl.capacity() == 10 );
		// 5
		assertTrue( cl.removeLast() == 53 );
		cl.capacity( 7 );
		// Re-allocate space to capacity = 7
		assertTrue( cl.capacity() == 7 );
		assertTrue( cl.get( 1 ) == 11 );
		assertTrue( cl.get( 2 ) == 13 ); // modified 
		// 6
		cl.addFirst( 29 );
		assertTrue( cl.size() == 6 );
		assertTrue( cl.getFirst() == 29 );
		// Uniform sample
		int sample = cl.sampleUniform();
	}
}
