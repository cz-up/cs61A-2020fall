HW_SOURCE_FILE=__file__

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 10:
        return 1 if x == 8 else 0 
    else:
        return num_eights(x//10) + 1 if x % 10 == 8 else num_eights(x//10)

def is_inc(n):
    if n <= 8:
        return True
    else:
        if (n - 1) % 8 == 0 or num_eights(n-1):
            return not is_inc(n-1)
        else:
            return is_inc(n-1)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 8:
        return n
    else:
        return pingpong(n-1) + 1 if is_inc(n) else pingpong(n-1) - 1


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    last, blast = n % 10, n // 10 % 10
    if n < 100:
        return 0 if last == blast else last - blast - 1
    else:
        return last - blast - 1 + missing_digits(n//10) if last - blast > 1 else missing_digits(n//10)


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_coin(coin):
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    #def change_helper(total, biggest):
    #    if total < 0:
    #        return 0 
    #    elif total < 5:
    #        return 1
    #    elif biggest == 1:
    #        return 1
    #    else:
    #        return change_helper(total-biggest, biggest) + change_helper(total, next_coin(biggest))
    #return change_helper(total, 25)
    def change_helper(total, smallest):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif smallest is None or smallest > total:
            return 0
        else:
            with_smallest = change_helper(total - smallest, smallest)
            without_smallest = change_helper(total, next_largest_coin(smallest))
            return with_smallest + without_smallest
    return change_helper(total, 1)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    #return 'YOUR_EXPRESSION_HERE'
    # fact = lambda n : 1 if n == 1 else mul(n, sub(n,1))
    """Function below is a lambda function which need two parameter
    parm 1 is a function f
    parm 2 is a x corresponding to factorial's x
    The lambda in the second parentheses is the input of first parenthese lambda
    i.e. the f in first parenthese.
    So the whole return sentence return a f(f,_) _ is the x in second lambda in first parenthese
    """
    #below two both work
    #return (lambda f:lambda x: f(f, x))(lambda f,x: 1 if x == 1 else x * f(f, x-1)) 
    return (lambda x:(lambda f:f(f,x))(lambda f,x: 1 if x == 1 else x * f(f, x-1)))

