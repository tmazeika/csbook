---
layout: default
title: Insertion Sort
---

|           | Best Case     | Average Case | Worst Case      |
| --------- | :-----------: | :----------: | :-------------: |
| **When**  | Sorted        | Random       | Reversed        |
| **Time**  | $$\Theta(n)$$ | $$O(n^2)$$   | $$\Theta(n^2)$$ |
| **Space** | $$O(1)$$      | $$O(1)$$     | $$O(1)$$        |

Insertion Sort works by *inserting* each element of an unsorted input array into a sorted output array. This is an in-place algorithm because it doesn't create a *new* output array, but rather maintains a sorted and unsorted region of the input array, mutating the array directly.

{% include video.html src="insertion-sort" %}

Additionally, the sort is stable because each element from left to right of the unsorted region gets inserted as far right into the sorted region as possible.

## Implementation

We start by iterating over the unsorted region of an input array of length $$n$$. Initially, the unsorted region is indices $$1$$ through $$n - 1$$. For each unsorted element $$x$$ at index $$i \geq 1$$, insert $$x$$ into the sorted region, which is always indices $$0$$ through $$i - 1$$. To find where to insert $$x$$, search backwards from index $$i - 1$$, shifting each element forward to make room for the eventual insertion of $$x$$, until we find an element that is less than or equal to $$x$$. The "or equal to" part is important for maintaining stability.

```python
def insertion_sort(arr):
# Iterate over the unsorted region, which starts at index 1.
    for i, x in enumerate(arr[1:], start=1):
        j = i - 1
# Search backwards for a place to insert x.
        while j >= 0 and x < arr[j]:
# Inside this loop, it holds that x comes before the current search position. Therefore, shift this element forward.
            arr[j + 1] = arr[j]
            j -= 1
# Outside the while loop, we've found the index at which to insert x.
        arr[j + 1] = x
    return arr

print(insertion_sort([]))           # []
print(insertion_sort([3, 2, 2, 8])) # [2, 2, 3, 8]
print(insertion_sort([7, 6, 4, 1])) # [1, 4, 6, 7]
```

## Analysis

Let's annotate each loop of the implementation with how many times it will run.

```python
def insertion_sort(arr):
    # (1) Runs exactly n - 1 times:
    for i, x in enumerate(arr[1:], start=1):
        j = i - 1
        # (2) Runs at most i times:
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr
```

Comment 1 says that the outer for loop runs $$n - 1$$ times. Comment 2 says that it takes at most $$i$$ iterations to insert every $$x$$ into the sorted region. Because that's a range and not an exact number, there are three cases to evaluate:

1. In the best case, there are no iterations. This happens when the first insertion position we check is the correct one, causing one comparison and no shifts. This means that the input array is already sorted.

    <p>
    \begin{equation}
       (n - 1) \times 1 \in \Theta(n)
    \end{equation}
    </p>

2. In the average case, there are $$i / 2$$ iterations. When the input array is in random order, some insertions of $$x$$ into the sorted region are quick, while others take some time. This averages out to looking back $$i / 2$$ positions.

    <p>
    \begin{equation}
        \sum_{i = 1}^{n - 1}\frac{i}{2} = \frac{n (n - 1)}{4} \in O(n^2)
    \end{equation}
    </p>

3. In the worst case, there are $$i$$ iterations. This occurs when every $$x$$ gets inserted at the head of the array, causing the most shifts and comparisons. This means that the array is in reverse order.

    <p>
    \begin{equation}
        \sum_{i = 1}^{n - 1}i = \frac{n (n - 1)}{2} \in \Theta(n^2)
    \end{equation}
    </p>

Generally, Insertion Sort is best for small or nearly-sorted arrays.

## Trivia

- At the end of $$k$$ iterations of the outer for loop, the first $$k + 1$$ elements of the input array are sorted.
