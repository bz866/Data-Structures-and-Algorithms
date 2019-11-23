
// The implementation of Circular List with generic type using Java

import java.util.ArrayList;
import java.util.Iterator;

public class CircularList<T> {

    protected ArrayList<T> _elements;
    protected int _capacity;
    protected int _tail; // tail reference
    protected int _head; // head reference
    protected int _size; // number of elements inside

    /**
     * Constructor
     * Make a circular list with an underlying array of type and a capacity
     */
    public CircularList( int capacity ) {
        _data = new ArrayList<T> ( capacity );
        for (int i = 0; i < capacity; i++ ) {
            _data.add(null);
        }
            _capacity = capacity;
            _head = 0;
            _tail = 0;
            _size = 0;
    }

    /** Append a value to the queue **/
    public void addLast( Type data ) {
        if( _size == _capacity )
            reallocate( _capacity * 2 );
        _data.set( _front, data );
        if( ( _front = _front + 1 ) == _capacity )
            _front = 0;
        _size++;
    }

    /** Make a new underlying array with capacity = newCapacity
     *  and copy all elements into the new space **/
    protected void reallocate( int newCapacity ) {
        if( ( newCapacity < _size ) || ( newCapacity <= 0 ) )
            throw new IndexOutOfBoundsException(
                    String.format(
                            "Can't resize circular of size %d to max capacity %d",
                            _size,
                            newCapacity
                    )
            );

        // Full queue
        // Re-allocate
        _capacity = newCapacity;
        ArrayList<Type> newArrayList = new ArrayList<Type>( _capacity );

        // Copy elements of old queue to new queue
        for( int i = 0; i < _size; i++ )
            newArrayList.add( this.get( i ) );

        // Fill the rest of the elements with null
        for( int i = _size; i < _capacity; i++ )
            newArrayList.add( null );

        // Reset all of the indices
        _front = _size;
        _back = 0;
        _data = newArrayList;
    }

    /** Retrieve an element at the i-th index of the queue **/
    public Type get( int i ) {
        if( ( i < 0 ) || ( i >= _size ) )
            throw new IndexOutOfBoundsException(
                    String.format(
                            "Index %d is out of bounds for circular list of size %d",
                            i,
                            _size
                    )
            );
        i = ( _back + i ) % _capacity ;
        return _data.get( i );
    }

    /** Remove element at the beginning of the queue **/
    public Type removeFirst() {
        Type value = this.get( 0 );
        _back = ( _back + 1 ) % _capacity;
        _size--;
        return value;
    }

    @Override
    public String toString() {
        Iterator<Type> dataIterator = _data.iterator();
        if( ! dataIterator.hasNext() )
            return "[]";
        StringBuffer buff = new StringBuffer();
        buff.append( "[" );
        buff.append( dataIterator.next() );
        while( dataIterator.hasNext() ) {
            buff.append( "," );
            buff.append( dataIterator.next() );
        }
        buff.append( "]" );
        return buff.toString();
    }

    /** Clear out all of the elements of the queue **/
    public void clear() {
        _size = 0;
        _back = 0;
        _front = 0;
    }

    /** Return number of elements in queue **/
    public int size() { return _size; }

    /** Return max capacity of the queue **/
    public int capacity() { return _capacity; }

    public Type getFirst() { return this.get( 0 ); }

    public Type getLast() { return this.get( _size - 1 ); }

    /** Prepend an element to queue **/
    public void addFirst(Type datum) {
        if( _size == _capacity )
            reallocate( _capacity * 2 );
        if( ( _back -= 1 ) < 0 )
            _back += _capacity;
        _data.set( _back, datum );
        _size++;
    }

    /** Remove an element from the end of the queue **/
    public Type removeLast() {
        Type value = this.getLast();
        if ( --_front < 0 )
            _front = _capacity - 1;
        --_size;
        return value;
    }

    /** Set the new capacity and compress the queue **/
    public void capacity(int newCapacity) {
        this.reallocate( newCapacity );
    }

    /** Get a uniform random sample from the queue **/
    public Type sampleUniform() {
        if( _size == 0 )
            throw new IndexOutOfBoundsException( "Can't sample when circular list is empty" );
        return this.get( (int) ( Math.random() * _size ) );
    }
}
