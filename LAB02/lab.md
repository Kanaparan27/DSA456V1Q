# Lab 2

### function 1:

Analyze the following function with respect to number

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

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1)) #6 

```

Time Complexity: O(1) 
Space Complexity: O(1)




### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

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

Analyze the following function with respect to number

```python
def function4(number): 
	total=1 #1
	for i in range(1 to number):  #(n-1)
		total=total*(i+1) #(0)1
	return total  #(0)1
```



​Time Complexity: O(n) 
Space Complexity: O(1)
