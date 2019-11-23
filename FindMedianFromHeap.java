// Your MedianFinder object will be instantiated and called as such:
// obj = MedianFinder()
// obj.addNum(num)
// param_2 = obj.findMedian()

// Find the median from the data stream 

import java.util.PriorityQueue;

class MedianFinder {

	private PriorityQueue<Integer> leftPQ = new PriorityQueue<Integer>( Collections.reverseOrder() );
	private PriorityQueue<Integer> rightPQ = new PriorityQueue<Integer> ();

	/**
	* add a number into the Finder, simulate the behavior of the data stream
	*
	*/
	public void addNum(int num) {
		// if the upper part is empty OR the num > the minimum of the upper part
		if ( this.leftPQ.isEmpty() || num <= leftPQ.peek() ) {
			this.leftPQ.offer( num );
		}
		else {
			this.rightPQ.offer( num ); 
		}

		// Rebalance the pqs
		if ( this.leftPQ.size() - this.rightPQ.size() > 1) {
			this.rightPQ.offer( this.leftPQ.poll() );
		}
		else if (this.rightPQ.size() - this.leftPQ.size() > 1) {
			this.leftPQ.offer( this.rightPQ.poll() );
		}
		else {}
	}

	/**
	* Return the median of current data stream
	*
	*/
	public double findMedian() {

		if ( this.leftPQ.isEmpty() && this.rightPQ.isEmpty() ) {
			throw new NoSuchElementException(); // if the queue is empty
		}

		if ( this.leftPQ.isEmpty() ){
			return (double) this.rightPQ.peek();
		}
		else if ( this.rightPQ.isEmpty() ) {
			return (double) this.leftPQ.peek();
		}
		else if ( this.leftPQ.size() > this.rightPQ.size() ) {
			return (double) this.leftPQ.peek();
		}
		else if ( this.rightPQ.size() > this.leftPQ.size() ) {
			return (double) this.rightPQ.peek();
		}
		else {
			return (double) ( this.leftPQ.peek() + this.rightPQ.peek() ) / 2;
		}
	}
}








