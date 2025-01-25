import random



class Algorithm:
    def run_algorithm(self, data: list) -> None:
        raise NotImplementedError("This method should be implemented")


def merge(data: list, left: int, mid: int, right: int):
    lenL, lenR = mid - left + 1, right - mid
    leftArr, rightArr = [0] * lenL, [0] * lenR
    for i in range(0, lenL):
        leftArr[i] = data[left + i]
    for i in range(0, lenR):
        rightArr[i] = data[mid + 1 + i]

    i, j, k = 0, 0, left
    # after comparing, we merge those two array
    # in larger sub array
    while i < lenL and j < lenR:
        if leftArr[i] <= rightArr[j]:
            data[k] = leftArr[i]
            i += 1

        else:
            data[k] = rightArr[j]
            j += 1

        k += 1
    # Copy remaining elements of left, if any
    while i < lenL:
        data[k] = leftArr[i]
        k += 1
        i += 1
    # Copy remaining element of right, if any
    while j < lenR:
        data[k] = rightArr[j]
        k += 1
        j += 1


def heapify(data: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[largest] < data[left]:
        largest = left
    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[largest], data[i] = data[i], data[largest]
        heapify(data, n, largest)


def partition(data: list, low: int, high: int):
    # choose the high element
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


class BubbleSort(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        for i in range(len(data)):
            swapCond = False
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapCond = True
            if not swapCond:
                break


class SelectionSort(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        for i in range(len(data) - 1):
            minId = i
            for j in range(i + 1, len(data)):
                if data[minId] > data[j]:
                    minId = j

            data[i], data[minId] = data[minId], data[i]


class InsertionSort(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        for i in range(1, len(data)):
            tempVal = data[i]
            j = i - 1
            while j >= 0 and tempVal < data[j]:
                data[j + 1] = data[j]
                j -= 1
                data[j + 1] = tempVal


class MergeSortIter(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        self.merge_sort(data, 0, len(data) - 1)

    def merge_sort(self, data: list, left: int, right: int):
        if left >= right:
            return
        midPoint = left + (right - left) // 2
        self.merge_sort(data, left, midPoint)
        self.merge_sort(data, midPoint + 1, right)
        merge(data, left, midPoint, right)


class MergeSortRecur(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        subSize = 1
        n = len(data)
        while subSize < n:
            left = 0
            while left < n:
                right = min(left + (subSize * 2 - 1), n - 1)
                mid = min(left + subSize - 1, n - 1)
                # need to account for final array which has a size not equal to a power of 2
                merge(data, left, mid, right)
                left += subSize * 2
            subSize *= 2


class HeapSort(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        n = len(data)
        # max heapify first, loop includes root
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        # loop does not include root since you are swapping it after every iteration, the last iteration will have the
        # minimum at the root already
        for i in range(n - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            heapify(data, i, 0)


class QuickSort(Algorithm):
    def run_algorithm(self, data: list) -> None:
        """Runs the algorithm on the provided data."""
        self.quick_sort(data, 0, len(data) - 1)

    def quick_sort(self, data: list, low: int, high: int):
        # start with low = 0 and high = len(data)-1
        if low < high:
            pivot = partition(data, low, high)
            self.quick_sort(data, low, pivot - 1)
            self.quick_sort(data, pivot + 1, high)


ALGORITHMS = (
    BubbleSort(), SelectionSort(), InsertionSort(),
    MergeSortIter(), MergeSortRecur(), HeapSort(), QuickSort()
)
ALGORITHM_NAMES = (
    'bubble_sort', 'selection_sort', 'insertion_sort', 'iterative_merge_sort',
    'recursive_merge_sort', 'heap_sort', 'quick_sort'
)

