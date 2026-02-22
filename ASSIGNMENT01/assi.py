import random
import time
import matplotlib.pyplot as plt

# Sorting algorithm 

def bubble_sort(my_list):
    """
    very simple bubble sort functio n.
    it change the list inside itself and return how many steps we do.
    in my counting idea:
       1 step when we compare two item
       3 step when we do swap
    """
    steps = 0
    n = len(my_list)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            # i count 1 step for this compare
            steps += 1
            if my_list[j] > my_list[j + 1]:
                # swap the two value, so i count 3 step (3 assign)
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3
    return steps


def selection_sort(my_list):
    """
    selection sort in simple way.
    here i always search minimum value for each position.
    steps idea---
       1 step for every compare in inner loop
       3 steps when i swap the min element with current one
    """
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            steps += 1  # compare two element
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            # here we do one swap, so i add 3 step
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            steps += 3
    return steps


def insertion_sort(mylist, left=0, right=None):
    """
    insertion sort.
    i made left and right optional so same function use for full list
    or just small part of the list also.
      insertion_sort
    i count steps like this:
       1 step when i take the key value
       1 step for each compare in while loop
       1 step when i shift value to right side
    """
    steps = 0
    if right is None:
        right = len(mylist) - 1

    # i goes from left+1 to right
    for i in range(left + 1, right + 1):
        key = mylist[i]
        steps += 1  # reading key value
        j = i - 1
        while j >= left:
            # here i mix the checks together and just count 1 step for compare
            steps += 1  # check j>=left and mylist[j] > key
            if mylist[j] > key:
                mylist[j + 1] = mylist[j]
                steps += 1  # shifting value to right
                j -= 1
            else:
                break
        mylist[j + 1] = key
        steps += 1  # putting key back in final place
    return steps


def _partition(arr, low, high, steps):
    """
    helper function for quick_sort.
    i just pick last element as pivot (easy but not best).
    step counting- - 
       1 step each time we compare with pivot
       3 steps for any swap we do
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        # compare arr[j] with pivot, so i add 1 step
        steps[0] += 1  # comparison arr[j] <= pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # here we swap two items, i count 3 step
            steps[0] += 3
    # finally put pivot in correct place in the middle
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps[0] += 3  # swap pivot also count as 3 step
    return i + 1


def _quick_sort_recursive(arr, low, high, steps):
    # normal recursive logic for quick sort, nothing fancy here
    if low < high:
        p = _partition(arr, low, high, steps)
        _quick_sort_recursive(arr, low, p - 1, steps)
        _quick_sort_recursive(arr, p + 1, high, steps)


def quick_sort(mylist):
    """
    quick sort.
    i use small list 'steps' so recursive function can change it (pass by refernce style).
    at the end i just return steps 0  as total step we did.
    """
    steps = [0]
    _quick_sort_recursive(mylist, 0, len(mylist) - 1, steps)
    return steps[0]



# Helper functions 
def make_best_case(n):
    """already sorted list [0, 1, 2, ..., n-1], so this is like best case."""
    return list(range(n))


def make_worst_case(n):
    """reverse sorted list [n-1, n-2, ..., 0], usually worst case for many sort."""
    return list(range(n - 1, -1, -1))


def make_average_case(n):
    """random order list, we can think as average case."""
    lst = list(range(n))
    random.shuffle(lst)
    return lst


# Step 1: basic test with list of length 10-0

def test_step1():
    # here i just check that all sort functions work fine for n = 100
    print("=== STEP 1: Basic sorting test (n = 100) ===")
    size = 100
    base_list = make_average_case(size)

    # Bubble sort
    b_list = base_list.copy()
    bubble_sort(b_list)
    print("Bubble sorted (first 10):", b_list[:10])

    # Selection sort
    s_list = base_list.copy()
    selection_sort(s_list)
    print("Selection sorted (first 10):", s_list[:10])

    # Insertion sort (whole list)
    i_list = base_list.copy()
    insertion_sort(i_list)  # using default left/right
    print("Insertion sorted (first 10):", i_list[:10])

    # Quick sort
    q_list = base_list.copy()
    quick_sort(q_list)
    print("Quick sorted (first 10):", q_list[:10])

    # small sanity check with built-in sorted list
    print("All same as built-in sorted? ->",
          b_list == sorted(base_list) == s_list == i_list == q_list)



# Step 2: T(n) for best / worst / average


def test_step2():
    # here i check T(n) values for different case with small n = 20
    print("\n=== STEP 2: T(n) for best, worst, average (n = 20) ===")
    n = 20

    for make_case, name in [(make_best_case, "Best (sorted)"),
                            (make_worst_case, "Worst (reverse)"),
                            (make_average_case, "Average (random)")]:
        print(f"\nCase: {name}")
        base = make_case(n)

        lst1 = base.copy()
        t_bubble = bubble_sort(lst1)

        lst2 = base.copy()
        t_selection = selection_sort(lst2)

        lst3 = base.copy()
        t_insertion = insertion_sort(lst3)

        lst4 = base.copy()
        t_quick = quick_sort(lst4)

        # just print the step count for each algo
        print("  Bubble sort T(n):   ", t_bubble)
        print("  Selection sort T(n):", t_selection)
        print("  Insertion sort T(n):", t_insertion)
        print("  Quick sort T(n):    ", t_quick)


# Step 3: Plot T(n) vs n for worst case

def measure_Tn(sort_func, sizes):
    """for every size in 'sizes', build worst case list and return T(n) list."""
    t_values = []
    for n in sizes:
        lst = make_worst_case(n)
        steps = sort_func(lst)
        t_values.append(steps)
    return t_values


def step3_plots():
    # this part will draw T(n) vs n graphs using our step counting
    print("\n=== STEP 3: Plot T(n) vs n (worst case) ===")

    # NOTE: O(n^2) sort are slow, so i dont go too big for them.
    small_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    quick_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

    # Bubble, selection, insertion
    bubble_T = measure_Tn(bubble_sort, small_sizes)
    selection_T = measure_Tn(selection_sort, small_sizes)
    insertion_T = measure_Tn(lambda arr: insertion_sort(arr), small_sizes)

    plt.figure()
    plt.plot(small_sizes, bubble_T, marker='o', label='Bubble')
    plt.plot(small_sizes, selection_T, marker='x', label='Selection')
    plt.plot(small_sizes, insertion_T, marker='s', label='Insertion')
    plt.xlabel("n (size of list)")
    plt.ylabel("T(n) steps (worst case)")
    plt.title("T(n) vs n for O(n^2) sorts (worst case)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Quick sort with bigger sizes because it faster normally
    quick_T = measure_Tn(quick_sort, quick_sizes)

    plt.figure()
    plt.plot(quick_sizes, quick_T, marker='o', label='Quick sort')
    plt.xlabel("n (size of list)")
    plt.ylabel("T(n) steps (worst case-ish)")
    plt.title("T(n) vs n for quick sort")
    plt.legend()
    plt.grid(True)
    plt.show()



# Step 4: Time the algorithms


def measure_time(sort_func, sizes):
    """for each size, measure real running time using time library (worst case)."""
    times = []
    for n in sizes:
        lst = make_worst_case(n)
        start = time.time()
        sort_func(lst)
        end = time.time()
        times.append(end - start)
    return times


def step4_plots():
    # this part draw time vs n graph, so we can compare with T(n) graph
    print("\n=== STEP 4: Plot running time vs n (worst case) ===")

    small_sizes = [10, 50, 100, 500, 1000, 5000, 10000]
    quick_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

    # Time O(n^2) sorts
    bubble_time = measure_time(bubble_sort, small_sizes)
    selection_time = measure_time(selection_sort, small_sizes)
    insertion_time = measure_time(lambda arr: insertion_sort(arr), small_sizes)

    plt.figure()
    plt.plot(small_sizes, bubble_time, marker='o', label='Bubble')
    plt.plot(small_sizes, selection_time, marker='x', label='Selection')
    plt.plot(small_sizes, insertion_time, marker='s', label='Insertion')
    plt.xlabel("n (size of list)")
    plt.ylabel("Time (seconds)")
    plt.title("Time vs n for O(n^2) sorts (worst case)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Time quick sort on bigger list sizes
    quick_time = measure_time(quick_sort, quick_sizes)

    plt.figure()
    plt.plot(quick_sizes, quick_time, marker='o', label='Quick sort')
    plt.xlabel("n (size of list)")
    plt.ylabel("Time (seconds)")
    plt.title("Time vs n for quick sort (worst case-ish)")
    plt.legend()
    plt.grid(True)
    plt.show()

# MaiN

if __name__ == "__main__":
    # Step 1: just check sorting works for n=100
    test_step1()

    # Step 2: check T(n) behaviour for best/worst/average
    test_step2()

    # Step 3: T(n) vs n plots (worst case)
    step3_plots()

    # Step 4: time vs n plots (worst case)
    step4_plots()