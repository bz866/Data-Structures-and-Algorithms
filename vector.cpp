# Implementation of vector ADT in STL counterpart

# include <algorithm>

template <typename object>
class Vector
{
public:
	explicit Vector(int initSize = 0) : theSize{initSize}, 
		theCapacity{initSize + SPARE_CAPACITY}
	{objects = new Object[theCapacity];}
	
	Vector(const Vector & rhs) :
