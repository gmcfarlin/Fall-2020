## Assignment2 ME369P
## Name: Grant McFarlin
## EID : gjm923

## Fill in the class and functions below.
## Make sure your class runs with the tests in main


'''
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]

kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: any non-square matrix will be random
                NOTE: different styles will always be square matrices
    format => string that will be formatted as 1st and last element of each row
'''
class myAwesomeMatrix(object):
    def __init__(self, *args, **kwargs):

        # Initialize values to defaults
        self.__dict__ = {'n': 0, 'i': 4, 'j': 4, 'set':[0,1], 'range': False, 'format': '', 'style': 'random'}
        # Import any user defined kwargs
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in self.__dict__.keys())

        # Handle n vs. i,j cases
        if len(args) == 2:
            self.i = args[0]
            self.j = args[1]
        elif len(args) == 1:
            self.i = args[0]
            self.j = args[0]
        elif self.n != 0:
            self.i = self.n
            self.j = self.n

        # Handle set vs. range cases
        if self.range:
            start, stop = self.range
            self.set = list(range(start, stop))

        # Add a space between the matrix and the format string
        if self.format:
            self.format += ' '

        # Generate appropriate matrix
        import random
        self.matrix = []

        for num_rows in range(self.i):
            row = []
            for num_cols in range(self.j):

                # Choose a random integer from the given set
                num_rand = self.set[random.randint(0,len(self.set)-1)]

                # Construct each row of matrix by style
                if self.style == 'lower':
                    row.append(num_rand if num_cols <= num_rows else 0)
                elif self.style == 'upper':
                    row.append(num_rand if num_cols >= num_rows else 0)
                elif self.style == 'diagonal':
                    row.append(num_rand if num_cols == num_rows else 0)
                elif self.style == 'symmetric':
                    # sym_element gets the appropriate element from the matrix if has been set already
                    sym_element = False if num_cols >= num_rows else self.matrix[num_cols][num_rows]
                    row.append(sym_element if sym_element else num_rand)
                else:
                    row.append(num_rand)

            # Store each row in the matrix attribute
            self.matrix.append(row)

    def __str__(self):

        string = ''

        for row in self.matrix:
            string_row = str(row).strip('[]').replace(',', '')
            string += self.format + string_row + self.format[len(self.format)::-1] + '\n'

        return(string)

    def oneNorm(self):
        # Max of the sum of all columns
        sums = []
        if len(self.matrix) == len(self.matrix[0]):
            for col in range(self.j):
                sum_col = 0

                for row in range(self.i):
                    sum_col += self.matrix[row][col]

                sums.append(sum_col)
            return(max(sums))
        else:
            print('Error! Matrix is not square')
            return(0)

    def infNorm(self):
        # Max of the sum of all rows
        sums = []
        if len(self.matrix) == len(self.matrix[0]):
            for row in range(self.i):
                sum_row = 0

                for col in range(self.j):
                    sum_row += self.matrix[row][col]

                sums.append(sum_row)
            return(max(sums))

        else:
            print('Error! Matrix is not square')
            return(0)

    def Add(self, other):
        # Assumes the other matrix was created as an instance of myAwesomeMatrix
        other = other.matrix

        new_matrix = []
        for row in range(self.i):
            new_row = []
            for col in range(self.j):
                #?? should I handle this error? can you add matrices of different sizes?
                if len(self.matrix) == len(other) and len(self.matrix[row]) == len(other[row]):
                    new_row.append(self.matrix[row][col] + other[row][col])

            new_matrix.append(new_row)

            # Generate string for new_matrix with same code as above, ensuring inheritance
            string = ''

            for row in self.matrix:
                string_row = str(row).strip('[]').replace(',', '')
                string += self.format + string_row + self.format[len(self.format)::-1] + '\n'

        return(string)

    def __add__(self, other):
        new_matrix = self.Add(other)
        return(new_matrix)

    def __lt__(self, other):
        if self.oneNorm() < other.oneNorm():
            return(True)
        else:
            return(False)


def calculatorA():

    while True:
        expression = input('Enter expression: ')
        result = 0.0

        if expression == 'q':
            break
        else:
            num1, operator, num2 = expression.split(' ')
            num1 = float(num1) if num1 != '' else 0.0
            num2 = float(num2) if num2 != '' else 0.0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2

        result = round(result,1)

        print(result)

def calculatorB():

    def calculate(num1,operator,num2):
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2

        result = round(result,1)
        return (result)

    while True:
        expression = input('Enter expression: ')
        result = 0.0
        operators = ['+','-','*','/','^']

        if expression == 'q':
            break
        elif expression == '':
            expression = '0 + 0'

        stuff = expression.split(' ')

        num1 = [float(stuff[0])]
        operator = [stuff[i] for i in range(1, len(stuff), 2)]
        num2 = [float(stuff[i]) for i in range(2, len(stuff), 2)]

        for i in range(len(stuff) // 2):
            result = calculate(num1[i], operator[i], num2[i])
            num1.append(result)
        print(result)


def calculatorC():
    ## Put code for question 2c in this function
    pass


if __name__ == '__main__':
    #Problem 1
    #Testing matrix constructions
    m = myAwesomeMatrix()
    print(m)
    kwargs = {'n': 4}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'i': 3, 'j': 4}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'n': 2, 'range': [1,2]}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'n': 2, 'set': [1, 2, 3], 'style':'lower'}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'n': 4, 'format': 'cool'}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'n': 4, 'style': 'diagonal', 'set': [1]}
    print(myAwesomeMatrix(**kwargs))
    kwargs = {'n': 5,'set': [5, 7, 8, 3, 2, 4, 9],'format':'ed!#','style':'symmetric'}
    print(myAwesomeMatrix(**kwargs))

    #Testing Addition with Add method
    kwargs = {'n': 4, 'style': 'upper', 'set': [4,3,6,7], 'format':'@-!-'}
    m2 = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    print('m2')
    print(m2)
    print('m2.Add(m)')
    print(m2.Add(m))

    #Testing Addition with overloaded add (+)
    print('m2 + m')
    print(m2+m)

    #Testing the matrix norms with square matrix
    kwargs = {'n': 6, 'set': [2,1,4,3,6,7]}
    m = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    print('1-norm of m =',m.oneNorm(),end='\n\n')
    print('Infinity-norm of m =',m.infNorm(),end='\n\n')

    #Testing the matrix norms with a matrix that isn't square
    kwargs = {'i': 6, 'j':2, 'set': [2,1,4,3,6,7]}
    m = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    m1N = m.oneNorm()
    print('1-norm of m =',m1N,end='\n\n')
    mNN = m.infNorm()
    print('Infinity-norm of m =',mNN,end='\n\n')

    #Testing overloaded '<' operator
    kwargs = {'n': 4, 'style': 'upper', 'set': [4,3,6,7]}
    m2 = myAwesomeMatrix(**kwargs)
    print('m2')
    print(m2)
    kwargs = {'n': 6, 'set': [0,1]}
    m = myAwesomeMatrix(**kwargs)
    print('m')
    print(m)
    print('It is', m < m2, 'that m is less than m2', end='\n\n')

    #Problem 2
    calculatorA()
    calculatorB()
    calculatorC()
    print("Done")

    # You can do any testing you want here
    # Anycode you run here will not run when being graded...
