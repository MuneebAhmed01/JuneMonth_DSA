#Find minimum elem in array(array can be rotated)
def small(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<arr[end]:
            res=arr[mid]
            end=mid-1
        else:
            start=mid+1
            res=arr[end]
    return res








arr = [4, 5, 6, 7, 0, 1, 2]




print(small(arr))