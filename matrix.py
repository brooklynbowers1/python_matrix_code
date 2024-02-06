from vector import Vector # Avoids vector.Vector every time

class Matrix(Vector):
    """this class creates Matricies from vectors and performs simple matrix operations and comparisons"""

    def __init__(self, vector_list):
        """a construtor method that creates a matrix from the Vector class
        :param vector_list: List of row vectors for the matrix, from earlier work
        :returns: no return for constructor"""
        
        # Check for an empty list of vectors
        if vector_list == []:
            raise ValueError('List of vectors cannot be empty.')

        # Check that everything in vector_list is an instance of our Vector class
        for v in vector_list:
            if not isinstance(v, Vector):
                raise TypeError("Matricies are created using vector entries")

        # Length of each vector is the number of columns in the matrix
        num_cols = vector_list[0].dim                                   # why do we have to index this?

        # Check that all vectors in vector_list are the same size
        for v in vector_list:
            if v.dim != num_cols:
                raise ValueError('Vectors must be of the same size.')

        ### TODO: Change the name of this if needed
        self.rows = vector_list

        
        # Store number of rows and columns for later
        # TODO: Check if this is legitmate!
        # use _variable for private variables, without underscore for @property
        self._num_cols = num_cols # We'll use this in @property num_cols later
        # Fix if needed self.num_cols = num_cols
        
        # TODO: Check if this is legitimate (and then you don't need @property)
        self._num_rows = len(vector_list)


    #a. Create a deep copy of a Matrix without importing copy
    # TODO: Check this later
    def __copy__(self):
        """ a method that creates a deep copy of the matrix
        :param self: a matrix composed of vectors created in the Vector class
        :returns: no return but stores a deep copy of the matrix"""

        temp = []
        for value in self:
            temp.append(value) # for each vector entry in self, place this entry into temp

        return Matrix(*temp) # stores a copy of the Matrix 


  #b. Print the Matrix in the format described in the test suite
  ### TODO: Come back and do this later!


  #c. Access an entry in Matrix M by entering M [row, column]
    def __getitem__(self, row, column):
        """
        Return the value at the given index.
        :param row: An integer index within range
        :param column: An integer index within range
        :return: The float value at position index
        """

        if isinstance(row, int) and isinstance(column, int):
            # the index (as an int) is greater than or equal to -length or strictly less than

            # Check that the row is within range (do we really want negative indices here?)
            if -self._num_rows <= row < self._num_rows:

                # Check that the column is in range
                if -self._num_cols <= row < self._num_cols:

                    # v = self.rows[row] is a row vector...
                    # then return v[column] to get an entry from that vector
                    return self.rows[row][column]

                else:
                    raise IndexError('...Column out of range')

            else:
                raise IndexError('...Row out of range')

        else:
            # Returns type error if row or columns number is not an int
            raise TypeError(f'Row and column positions must be an integer index.')


  #d. Change an entry in Matrix M by entering M [row, column] = value

    def __setitem__(self, row, column, value):      # TODO: Check syntax for multiple dimensions
        """
        Return the value at the given index.
        :param row: An integer index within range
        :param column: An integer index within range
        :return: The float value at position index
        """

        if not isinstance(value, (int, float)):
            # raises type error if value is not a numerical entry
            raise TypeError('A Matrix can have only numerical entries.')

			# converting individual value in data to float
            self.data[index] = float(value)

        if isinstance(row, int) and isinstance(column, int):
            # the index (as an int) is greater than or equal to -length or strictly less than

            # Check that the row is within range (do we really want negative indices here?)
            if -self._num_rows <= row < self._num_rows:

                # Check that the column is in range
                if -self._num_cols <= row < self._num_cols:

                    # v = self.rows[row] is a row vector...
                    # Grab the right row vector
                    v = self.rows[row]

                    # Change the entry in that vector
                    v[column] = float(value)

                    # Replace the old row with the changed vector
                    self.rows[row] = v

                else:
                    raise IndexError('...Column out of range')

            else:
                raise IndexError('...Row out of range')

        else:
            # Returns type error if row or columns number is not an int
            raise TypeError(f'Row and column positions must be an integer index.')


  #e. get_row(row): Return an entire given row of Matrix as a Vector

    def get_row(self, row)              ### do we need self here??    

        if isinstance(row, int):
            # the index (as an int) is greater than or equal to -length or strictly less than

            # Check that the row is within range (do we really want negative indices here?)
            if -self._num_rows <= row < self._num_rows:

                # v = self.rows[row] is a row vector...
                    # then return v[column] to get an entry from that vector
                    return self.rows[row][column]



  #f. get_column(column): Return an entire given column of Matrix as a Vector



  #g. set_row(index, vector): Replace an existing row with a new Vector
    def set_row(index, row)              ### do we need self here??    

        if isinstance(row, int):
            # the index (as an int) is greater than or equal to -length or strictly less than

            # Check that the row is within range (do we really want negative indices here?)
            if -self._num_rows <= row < self._num_rows:

                # v = self.rows[row] is a row vector...
                    # then return v[column] to get an entry from that vector
                    return self.rows[row][column]



  #h. set_column(index, vector): Replace an existing column with values specified by a
    #new Vector



  #i. Add and subtract matrices using + and –



  #j. Multiply all reasonable options in all appropriate orders:
    #i. self * scalar



    #ii. scalar * self



    #iii. self * Matrix (Why do we not need a special case for Matrix * self?)



    #iv. self * Vector



    #v. Vector * self
        #Note: In iv, the vector is thought of as a column vector. This is the usual
          #approach in right-handed coordinate systems. In v, the vector is thought of
            #as a row vector. This is usually used in left-handed coordinate systems.



  #k. Return the negative of a matrix using –



  #l. Check whether two matrices are equal



  #m. det(): Return the determinant of a 2 x 2, 3 x 3, or 4 x 4 Matrix




  #n. transpose(): Given a Matrix of any dimension, not necessarily square, return its
    #transpose
