import random
import time

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1, comparisons

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]
    print(f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comparisons':>16} {'BS Comparisons':>16}")
    print('-' * 75)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search timing
        start = time.perf_counter()
        for _ in range(100):
            _, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search timing
        start = time.perf_counter()
        for _ in range(100):
            _, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>16} {comp_bs:>16}")


arr = []
n=int(input("enter no array entries"))
for i in range(n):
    iin=int(input("enter your element"))
    arr+=[iin]
    
target = int(input("enter your target number"))
idx, comps = interpolation_search(arr, target)
print(f"Array: {arr}")
print(f"Searching for: {target}")
print(f"Found at index: {idx}, Comparisons: {comps}\n")

performance_analysis()
