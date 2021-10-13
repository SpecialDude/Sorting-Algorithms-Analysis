from inspect import getmembers, isfunction

class Sorting:

    @staticmethod
    def bubbleSort(array):
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[j] < array[i]:
                    array[j], array[i] = array[i], array[j]

    @staticmethod
    def bubbleSort2(array):
        sort = True
        while sort:
            sort = False
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    sort = True

    @staticmethod
    def insertionSort(array):
        """for i in range(len(array)):
            k = i
            for j in range(i-1, -1, -1):
                if array[k] < array[j]:
                    array[j], array[k] = array[k], array[j]
                    k -= 1
                    continue
                break"""

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1;
            while (j > -1 and array[j] > key):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

    @staticmethod
    def selectionSort(array):
        for i in range(len(array)):
            small = i
            for j in range(i+1, len(array)):
                if array[j] < array[small]:
                    small = j
            array[i], array[small] = array[small], array[i]

    @staticmethod
    def quickSort(array):
        def partiton(array, p, r):
            x = array[r]
            i = p - 1

            for j in range(p, r):
                if array[j] <= x:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            
            array[i + 1], array[r] = array[r], array[i + 1]
            return i + 1
        
        def quickSorting(array, p, r):
            if p < r:
                q = partiton(array, p, r)
                quickSorting(array, p, q - 1)
                quickSorting(array, q + 1, r)
        
        quickSorting(array, p=0, r=len(array) - 1)
    
    @staticmethod
    def radixSort(array):
        def makeBucket(num):
            return [[] for _ in range(num)]
        
        def mergeBucket(bucket):
            b = []
            for i in bucket:
                b += i
            return b
        
        maxDigit = 1
        n = 0
        
        while n < maxDigit:
            bucket = makeBucket(10)
            for i in range(len(array)):
                strNum = len(str(array[i]))
                if n >= strNum:
                    digit = 0
                else:
                    digit = int(str(array[i])[(n + 1) * -1])
                bucket[digit].append(array[i])
                
                if strNum > maxDigit:
                    maxDigit = strNum
            n += 1
            array = mergeBucket(bucket)
        return array
    
    @staticmethod
    def bucketSort(arr):
        def bucketSorting(arr, noOfBuckets):
            max_ele = max(arr)
            min_ele = min(arr)

            # range(for buckets)
            rnge = (max_ele - min_ele) / noOfBuckets

            temp = []

            # create empty buckets
            for i in range(noOfBuckets):
                temp.append([])

            # scatter the array elements
            # into the correct bucket
            for i in range(len(arr)):
                diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

                # append the boundary elements to the lower array
                if (diff == 0 and arr[i] != min_ele):
                    temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

                else:
                    temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

            # Sort each bucket individually
            for i in range(len(temp)):
                if len(temp[i]) != 0:
                    temp[i].sort()

            # Gather sorted elements
            # to the original array
            k = 0
            for lst in temp:
                if lst:
                    for i in lst:
                        arr[k] = i
                        k = k + 1
        bucketSorting(arr, 10)
    
    @staticmethod
    def heapSort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l
            
            if r < n and arr[largest] < arr[r]:
                largest = r
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        
        n = len(arr)

        for i in range(n//2, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    @staticmethod
    def mergeSort(arr):
        def merge(Arr, start, mid, end):
            temp = [0] * (end - start + 1)
            i, j, k = start, mid+1, 0

            while(i <= mid and j <= end) :
                if(Arr[i] <= Arr[j]) :
                    temp[k] = Arr[i]
                    k += 1; i += 1
                else :
                    temp[k] = Arr[j]
                    k += 1; j += 1
            
            while(i <= mid) :
                temp[k] = Arr[i]
                k += 1; i += 1

            while(j <= end) :
                temp[k] = Arr[j]
                k += 1; j += 1

            for i in range (start, end+1):
                Arr[i] = temp[i - start]

        def mergeSorting(arr, start, end):
            if(start < end) :
                mid = (start + end) // 2
                mergeSorting(arr, start, mid)
                mergeSorting(arr, mid+1, end)
                merge(arr, start, mid, end)
        
        mergeSorting(arr, 0, len(arr) - 1)

             
    

Sorting.bubbleSort.__name__ = "Bubble Sort"
Sorting.bubbleSort2.__name__ = "Bubble Sort (Bad)"
Sorting.insertionSort.__name__ = "Insertion Sort"
Sorting.selectionSort.__name__ = "Selection Sort"
Sorting.quickSort.__name__ = "Quick Sort"
Sorting.bucketSort.__name__ = "Bucket Sort"
Sorting.heapSort.__name__ = "Heap Sort"
Sorting.mergeSort.__name__ = "Merge Sort"
Sorting.radixSort.__name__ = "Radix Sort"



algorithms = [member for name, member in getmembers(Sorting) if isfunction(member)]

def getAlgorithmNames():
    return [algorithm.__name__ for algorithm in algorithms]

def getAlgorithm(filter = None):
    return [algorithm for algorithm in algorithms if filter == None or algorithm.__name__ in filter]
