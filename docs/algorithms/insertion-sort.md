---
layout: default
title: Insertion Sort
---

Insertion Sort works by *inserting* each element of an unsorted input array into a sorted output array. This is an in-place algorithm because it doesn't create a *new* output array, but rather maintains a sorted and unsorted region of the input array.

{% include video.html src="insertion-sort" %}

## Implementation

We'll start by iterating over the unsorted region of an input array of length $$n$$. Initially, the unsorted region is indices $$1$$ through $$n - 1$$. For each unsorted element $$x$$ at index $$i \geq 1$$, insert $$x$$ into the sorted region, which is always indices $$0$$ through $$i - 1$$. To find where to insert $$x$$, search backwards from index $$i - 1$$, shifting each element forward to make room for the eventual insertion of $$x$$, until we find an element that is less than or equal to $$x$$. The "or equal to" part is important for maintaining stability.

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

## Trivia

- At the end of $$k$$ iterations of the outer `for`-loop, the first $$k + 1$$ elements of the input array will have been sorted.
