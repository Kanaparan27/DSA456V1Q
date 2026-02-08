Part B Analysis

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
Work each call only few if checks and one multiply, so constant work.
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


Need 2 count functions.
function2(mystring)

It only does len(mystring) one time then it call recursive_function2 one time So:

F(n) = R(n) + c

recursive_function2(mystring, a, b) base case when a >= b (means we reached middle) if not base case, it compare 2 characters then call itself with a+1 and b-1

So it moves inside by 1 from both side. That means the size go down by 2 each call.
How many calls? around n/2 calls until meet in middle.

So: R(n) = R(n-2) + c

Time = O(n)
Stack (depth) = O(n)





Part C Reflection
Describe how to approach writing recursive functions; what steps do you take?

The first thing I look for when writing a recursive function is the smallest case. such as if the list is empty or the number is 0. My base case is that. In order to prevent the function from calling itself indefinitely, I always write the base case first. I then consider ways to reduce the issue. Move the index to the following position in a list when the factorial is n-1. The problem is that the recursive call needs to use the same function but with less data. Every time it approaches the base case, I also make sure of that.
I create a helper function inside if the problem requires additional tracking because it facilitates recursion. I start by testing small inputs (0, 1, empty list, one item).


Describe the process of analyzing recursive functions. How does it differ from analyzing non-recursive functions? How is it the same?

The first thing I do when analysing a recursive function is determine the input size, such as n = number, n = len(list), or n = len(string). After that, I examine the function to see what it accomplishes with a single call (such as a single multiply or a few comparisons). I then examine the recursive call to observe how the input decreases with each iteration, such as n-1, n-2, or n/2. Next, I write a basic rule such as T(n) = T(n-1) + c or T(n) = T(n/2) + c. Lastly, I determine the Big-O by counting the number of times it will call until it reaches the base case. Since more calls equate to more stack memory, I also look at the recursion depth.
It differs from non-recursive analysis in that the former typically involves counting loops (for and while loops) and adding up operations within the loop. Since there is no obvious loop in recursion, I use a recurrence relation to count the number of recursive calls. Stack depth is crucial because recursion uses more memory due to the call stack.
