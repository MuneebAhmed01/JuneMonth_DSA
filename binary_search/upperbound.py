def upper(arr,n):
    low=0
    high=len(arr)-1
    res=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=n:
            low=mid+1        
            res=arr[mid+1]
        elif arr[mid]>n:
            high=mid-1
        
    return res






arr=[2,5,8,12,15,18,20,25]
n=15
print(upper(arr,n))