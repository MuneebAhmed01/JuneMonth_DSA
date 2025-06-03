# Count number of occurance of element in array

def occur(arr,target):
    start=0
    end=len(arr)-1
    res=0
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<target:
            start=mid+1
        elif arr[mid]==target:
            end=mid-1
            res=mid
        else:
            end=mid-1
    return res

def occur2(arr,target):
    start=0
    end=len(arr)-1
    res=0
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<target:
            start=mid+1
        elif arr[mid]==target:
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res






arr=[1,3,4,7,8,10,10,10,10,10,10,10,10,10,10,10,15,18,19]
target=10
hello=occur(arr,target)
hello_end=occur2(arr,target)
print(hello_end-hello+1)