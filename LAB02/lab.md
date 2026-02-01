# Lab 2

### function 1:

```python
def function1(number): 
	total=0;     //1

	for i in range(0,number):  # 1 , n
		x = (i+1)     # n
			total += x * x  # 2n

	return total  #1
```
    1+(n)+n+2n+1 = 4n+2.

	Time Complexity: O(n) 
	Space Complexity: O(n)
      
### function 2:

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1)) #6 

```

Time Complexity: O(1) 
Space Complexity: O(1)


### function 3:


def function3(list): 
	for i in range (0,len(list)-1):    #(n-1)
		for j in range(0,len(list)-1-i):  #(n-1)
			if(list[j]>list[j+1]):  #(n-1) , (n-2)....
				tmp=list[j]
				list[j]=list[j+1] #3
				list[j+1]=tmp

```
 (n-1)n /2  = n2-2/2


​Time Complexity: O(n2) 
Space Complexity: O(n2)

### function 4:

```python
def function4(number): 
	total=1 #1
	for i in range(1, number):  #(n-1)
		total=total*(i+1) #(0)1
	return total  #(0)1
```



​Time Complexity: O(n) 
Space Complexity: O(1)


Part C — In-Lab Discussion
Group Members

Kanaparan (Me)

Nikash

Timing Data
Team member	Timing for fibonacci	Timing for sum_to_number
Kanaparan (Me)	0.0000049	0.4294699
Nikash	0.0	0.0
Summary
function	fastest	slowest	difference
sum_to_number	0.0	0.4294699	0.4294699
fibonacci	0.0	0.0000049	0.0000049


Reflection


According to the findings, performance variations were primarily caused by the methodology employed rather than minor syntactic variations. Because the fibonacci function was implemented using an iterative loop, which eliminates the need for repetitive recalculations, it operated incredibly quickly. This maintains a very short execution time and a linear temporal complexity.
Sum_to_goal, on the other hand, took a lot longer. It conducts repeated adds inside the loop, which increases runtime as the input expands even though it is still efficient. It just does more work per call than Fibonacci ,d
Both methods employ a tiny and consistent amount of memory in terms of space use. A recursive method, which some students employed, would utilize more memory due to the function call stack, whereas the iterative fibonacci uses only a few variables.
Ultimately, the most important lesson is that algorithm selection is more important than small code details. Performance can be significantly increased by avoiding needless recursion and repetition.