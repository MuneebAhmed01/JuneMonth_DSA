# def lower(arr,target,low,high):
#     while low<=high:
#         mid=(low+high)//2
        
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#            return lower(arr,target,mid+1,high)
#         elif arr[mid]>target:
#            return lower(arr,target,low,mid-1)
#     return-1


     


# arr=[2,5,8,11,15,19]
# high=len(arr)-1
# low=0
# target = 11
# print(lower(arr,target,low,high))







def lower(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1  
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            result = arr[mid]    
            high = mid - 1        
        else:
            low = mid + 1         

    return result

arr=[1,4,6,8,9,11,16,119]
Target=3
print(lower(arr,Target))
