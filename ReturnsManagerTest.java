package QuestionTwo;

import static org.junit.Assert.*;

import org.junit.Test;
import java.util.Random;
import java.util.ArrayList;
import java.util.Collections;
import java.lang.reflect.Method;


public class ReturnsManagerTest {

	@Test
	public void testReturnsManager() {
		ReturnsManager testReturnsManager = new ReturnsManager( 100 );
	}

	@Test
	public void testAdd() {
		Random randomizer = new Random();
		ReturnsManager testReturnsManager = new ReturnsManager( 10 );
		// 10 returns 
		for (int i = 0; i < 10; i++ )
		{
			testReturnsManager.add( randomizer.nextDouble() )	;
		}
	}
	

	@Test
	public void testGetLast() {
		ReturnsManager testReturnsManager = new ReturnsManager( 3 );
		for (double i = 0; i < 5; i++ )
		{
			testReturnsManager.add( i )	;
		}
		// 3 returns, [3.0, 4.0(tail), 2.0(head)]
		assertTrue( testReturnsManager.getLast() == 4.0 );
	}

	@Test
	public void testGetLower() {
		ReturnsManager testReturnsManager = new ReturnsManager( 10 );
		for (double i = 0; i < 12; i++ )
		{
			testReturnsManager.add( i/2.0 )	;
		}
		// reference output
		ArrayList<Double> refOne = new ArrayList<Double>(5);
		refOne.add( 1.5 );
		refOne.add( 1.0 );
		refOne.add( 2.0 );
		Collections.sort( refOne );
		// output
		ArrayList<Double> output = testReturnsManager.getLower( 2.0, 6 );
		Collections.sort( output );
		// ArrayList [1.5, 1.0, 2.0]
		assertTrue( output.equals( refOne ));
	}

	@Test
	public void testGetHigher() {
		ReturnsManager testReturnsManager = new ReturnsManager( 10 );
		for (double i = 0; i < 12; i++ )
		{
			testReturnsManager.add( i/2.0 )	;
		}
		// reference output
		ArrayList<Double> refOne = new ArrayList<Double>(5);
		refOne.add( 5.0 );
		refOne.add( 5.5 );
		refOne.add( 4.0 );
		refOne.add( 4.5 );
		Collections.sort( refOne );	
		// output
		ArrayList<Double> output = testReturnsManager.getHigher( 4.0, 6 );
		Collections.sort( output );
		// ArrayList [4.5, 4.0, 5.0, 5.5 ]
		assertTrue( output.equals( refOne ));
	}
}
