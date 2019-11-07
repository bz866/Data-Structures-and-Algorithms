
template<class T> class Vector
{
  public:
    // ------ CONSTRUCTORS -----
    // Default constructor
    Vector();
    explicit Vector( int s );
    
    // Copy constructor
    Vector( const Vector& arg);
    
    // Copy Assignment
    Vector<T>& operator = (const Vector<T>& arg);
  
    // Destructor
    ~Vector();
    
    // ----- ITERATORS -----
    class iterator;
  
    iterator begin();
    
    const iterator begin() const;
  
    iterator end();
  
    const iterator end() const;
  
    const iterator cbegin() const;
  
    const iterator cend() const;
  
