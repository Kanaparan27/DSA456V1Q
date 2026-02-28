Kanaparan Arudchelvan
Nikash Sritharan

 PART A

1.
He was trying to improve `std::sort`, which is usually implemented as introsort (a mix of quicksort, heapsort, etc.).
The main focus was improving the quicksort partitioning part and also the small-range insertion sort part.

2
Microsoft Visual Studio switches to insertion sort at around 32 elements.

3
GNU’s implementation switches to insertion sort at around 16 elements.

4
Even though binary search reduces comparisons from O(n) to O(log n):

 Insertion sort still has to shift elements, which costs O(n).
 The main cost is data movement, not comparisons.
*Binary search also adds extra branching, which can hurt branch prediction.

5
Branch prediction is a CPU optimization technique where the processor tries to guess the result of conditional branches so it can avoid pipeline stalls.

6
Informational entropy measures how much uncertainty is in the data.
A random array has high entropy.
A nearly sorted array has low entropy.

7
Unguarded insertion sort removes boundary checking fully.

```
while (j > 0 && a[j-1] > value)   // regular insertion sort
```

By removing some of these checks, there are fewer branch instructions and less checking, so it runs faster on modern CPUs.

8
He suggests removing branches like:


if (x < y)
    min = x;
else
    min = y;


Instead, he prefers arithmetic tricks to avoid branching. For example:


min = y ^ ((x ^ y) & -(x < y));


This way you avoid unpredictable `if` statements and the CPU can use conditional moves instead.

9
The bug happened in GNU’s introsort when:

 Partitioning created very unbalanced partitions.
 The recursion depth handling failed in some rare cases.
 The algorithm could degrade close to quadratic time.

It was related to incorrect pivot handling and recursion depth control in special edge cases.

10 n the graphs, when the threshold increases, the number of comparisons and the number of moves both increase, but the actual running time goes down. This looks confusing if we only measure comparisons and moves. The speaker explains that we are missing an important metric: how often the CPU guesses a branch wrong.


11
Fast code keeps execution in a predictable path and avoids deep nesting.
It tries to reduce unpredictable branches and prefers straight-line execution as much as possible.

“Left-leaning” means using early exits and avoiding too many nested conditionals.
The control flow becomes simpler and easier for the CPU to predict.

That is why he says fast coding is left leaning.

12
Hot code means code that runs very often and is performance critical.
Cold code means code that runs rarely, like error handling parts.

If you mix hot and cold code together, it can cause CPU cache pollution and confuse the branch predictor, which may reduce performance.

Reflection

1..Understanding how minor adjustments to the sorting algorithm can result in significant speed differences was the most difficult aspect of the video. He was discussing CPU cache, branch prediction, and low level behavior, which confused me a little because I always believed that Big O complexity was the most important factor. It was challenging to completely comprehend how hardware impacts algorithm performance.

2.The most unexpected thing I discovered is that in practice, algorithms with higher time complexity are not always faster. I had no idea that code on paper could occasionally run quicker due to the way the processor operates. Additionally, I was shocked to see that even little microoptimizations could result in significant performance gains.


3.Yes, the movie pushed me to create code more quickly and effectively. In the future, I'll consider how the code actually operates on the computer in addition to Big O. Rather than assuming my code is fast, I intend to test and measure it more. I'll also make an effort to build loops that are cleaner and focus more on data movement and memory access. 
