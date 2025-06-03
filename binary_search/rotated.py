
#FInd element in rotated arry
def rotate(arr,target):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        if arr[start]>arr[mid]:
            if arr[mid]<target<=arr[end]:
                start=mid+1
            else:
                end=mid-1
        else:
             if arr[start]<=target<arr[mid]:
                 end=mid-1
             else:
                 start=mid+1
    return -1
                


    



arr=[81,86,89,96,99,20,25,43,56,62,74]
target=86
print(rotate(arr,target))