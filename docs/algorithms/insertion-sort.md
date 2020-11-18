---
layout: default
title: Insertion Sort
---

Insertion Sort works by *inserting* each element of an unsorted input array into a sorted output array. This is an in-place algorithm because it doesn't create a *new* output array, but rather maintains a sorted and unsorted region in the input array.

{% include video.html src="insertion-sort" %}

## Implementation

Working bottom-up, we'll start by inserting an element into an already sorted array.

```python
def insert(x, arr):
# Inserting x into an empty array results in an array with x by itself.
    if len(arr) == 0: return [x]
# When x is less than or equal to the head of the array (i.e. the smallest element), the result is x followed by the array.
    elif x <= arr[0]: return [x] + arr
# Otherwise, the result is the head of the array followed by the result of inserting x somewhere into the tail of the array.
    else: return [arr[0]] + insert(x, arr[1:])

print(insert(1, []))        # [1]
print(insert(1, [-1]))      # [-1, 1]
print(insert(1, [2, 2, 3])) # [1, 2, 2, 3]
print(insert(5, [1, 2, 9])) # [1, 2, 5, 9]
```

Now we'll need to iterate over the input array and insert each element into some sorted array.

```python
def sort(arr):
# An empty array is already sorted.
    if len(arr) == 0: return []
# Otherwise, insert the head of the array into the sorted tail.
    else: return insert(arr[0], sort(arr[1:]))

print(sort([]))              # []
print(sort([1]))             # [1]
print(sort([1, 5, 2, 2, 3])) # [1, 2, 2, 3, 5]
```

The recursive case may be a bit confusing, so let's dig in some more. First, notice that calling `insert` with the head of an array and its own tail results in a new array with all the same elements as the original, albeit in a different order. Fortunately, `insert` also guarantees that if we give it a sorted array in which to insert an element, we'll get *back* a sorted array. We use that property to our advantage: just return the result of inserting the head into the *sorted* tail. The tail isn't necessarily sorted yet, but recall that we have a function that sorts arrays: `sort`!
