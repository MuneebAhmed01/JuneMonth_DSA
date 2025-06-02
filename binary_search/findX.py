# Binary Search to find X in sorted array X is let say 6

def binary(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found

        elif arr[mid] < target:
            left = mid + 1  # Search in the right half

        else:
            right = mid - 1 

arr=[0,1,2,3,4,5,6,7,8,9]
target=int(input("enter number"))
print(binary(arr,target))
    


