#bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        swapped = False
    
        for j in range(n -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original:", numbers)
bubble_sort(numbers)
print("Swapped:", numbers)
