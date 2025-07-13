# quick_merge_compare.py

# 1. Import modules
import time
import random
import tracemalloc

# 2. Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 3. Merge Sort Function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 4. Test Function
def test_sort(sort_function, data):
    tracemalloc.start()
    start_time = time.time()
    sort_function(data.copy())
    end_time = time.time()
    memory_current, memory_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, memory_peak / 1024  # in KB

# 5. Performance Comparison
def compare_algorithms():
    dataset_sizes = [1000, 5000, 10000]
    for size in dataset_sizes:
        datasets = {
            "Sorted": list(range(size)),
            "Reverse Sorted": list(range(size, 0, -1)),
            "Random": random.sample(range(size * 2), size)
        }
        for dtype, data in datasets.items():
            qt, qm = test_sort(quick_sort, data)
            mt, mm = test_sort(merge_sort, data)
            print(f"\nSize: {size} | Type: {dtype}")
            print(f"Quick Sort -> Time: {qt:.5f}s | Memory: {qm:.2f}KB")
            print(f"Merge Sort -> Time: {mt:.5f}s | Memory: {mm:.2f}KB")

# 6. Run Comparison
if __name__ == "__main__":
    compare_algorithms()
