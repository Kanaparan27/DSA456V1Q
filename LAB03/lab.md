Part B Analysis
Function 1
def function1(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        return value * function1(value, number-1)


Analysis (based on number = n)

When number is 0 or 1, it stops (base case).

When number is bigger, it call itself with number-1.

So it reduce by 1 every time.

How many calls?

n, n-1, n-2, ... 1

that is about n calls

Work each call

only few if checks and one multiply, so constant work.

So total:

T(n) = T(n-1) + c

Time = O(n)

Stack (recursion depth) = O(n)

Function 2
def recursive_function2(mystring,a, b):
    if(a >= b ):
        return True
    else:
        if(mystring[a] != mystring[b]):
            return False
        else:
            return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
    return recursive_function2(mystring, 0,len(mystring)-1)


Analysis (based on length of string = n)

Need 2 count functions.

1) function2(mystring)

It only does len(mystring) one time

then it call recursive_function2 one time

So:

F(n) = R(n) + c

2) recursive_function2(mystring, a, b)

base case when a >= b (means we reached middle)

if not base case, it compare 2 characters

then call itself with a+1 and b-1

So it moves inside by 1 from both side.
That means the size go down by 2 each call.

How many calls?

around n/2 calls until meet in middle.

So:

R(n) = R(n-2) + c

this becomes linear

Final:

Time = O(n)

Stack (depth) = O(n)

Function 3 (optional)
def function3(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        half = number // 2
        result = function3(value, half)
        if (number % 2 == 0):
            return result * result
        else:
            return value * result * result


Analysis (based on number = n)

Each time it call itself with number//2

so number become half every time.

How many calls?

n, n/2, n/4, n/8, ... 1

that is about log2(n) calls

Work per call is constant (some if checks, multiply).

So:

T(n) = T(n/2) + c

Time = O(log n)

Stack (depth) = O(log n)