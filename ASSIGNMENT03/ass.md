Analysis of SortedTable

In this part I am looking at the time complexty of the functions in the SortedTable class.

Let n be the number of records in the table.

insert(self, key, value)

The time complexity of insert is O(n^2).

First it calls search(key) to check if the key is already inside the table. That search takes O(n) time.

Then if the table is full, it makes a new bigger table and copies all the old values into that new table, so that part is also O(n).

After that it adds the new record at the end and then uses bubble sort to sort the table again. Bubble sort takes O(n^2) time.

So because of the bubble sort part, the final time complexity is O(n^2).

modify(self, key, value)

The time complexity of modify is O(n^2).

At first this function looks like just a simple linear search, so it may look like O(n), but it is actually slower in this code.

The reason is because inside the while loop it keeps calling len(self). The len function is not O(1) here. It goes through the full table and counts the records one by one, so len(self) is O(n).

Since the loop may run up to n times, and len(self) is being checked again and again, the total time becomes O(n^2).

So even though it looks small, this part makes it slower then expected.

remove(self, key)

The time complexity of remove is O(n).

First it gets the size by calling len(self), and that takes O(n).

Then it searches for the key, and that also takes O(n).

If the key is found, it shifts all the records after that position one step to the left. That shifting can also take O(n).

So the overall time complexty is still O(n).

search(self, key)

The time complexity of search is O(n).

First it gets the size using len(self), and len(self) takes O(n).

Then it does a linear search through the records until it finds the key or reaches the end of the table.

So the total is O(n).

capacity(self)

The time complexity of capacity is O(1).

This is because it only returns self.cap.

There is no loop and no extra work done in this function.

len(self)

The time complexity oflen is O(n).

This function goes through the whole list and counts how many values are not None.

Because it checks all the spots in the table, it takes O(n) time.

Ways to make SortedTable better

I think this code works, but it is not very effecient.

One thing that can be improved is storing the number of records in a variable like size. Then len would nt need to count everything every single time, and it can become O(1).

Another thing is using binary search. Since the table is already sorted, doing a normal linear search is kind of wasting time. Binary search would make search faster.

Also for insert, instead of adding the record at the end and sorting the whole used part again with bubble sort, it would be better to find the correct position first and then shift the records. That would be much better then sorting everything again.

So the code can be improved by storing the size, using binary search, and not using bubble sort after every insert.

Conclusion

The slowest function in this class is insert() because of the bubble sort, so it is O(n^2).

modify() also becomes O(n^2) because of the repeated calls to len(self) inside the loop.

The other main functions are mostly O(n), and capacity() is O(1).
