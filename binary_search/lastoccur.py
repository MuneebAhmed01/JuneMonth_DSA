#find the last occurance of element in array
def occur(arr,target):
    start=0
    end=len(arr)-1
    res=-1
    while start<=end:
        mid = (start+end)// 2

        if arr[mid]==target:
            res=mid
            start=mid+1
        elif arr[mid]>target:
             end=mid-1


        else:
            start=mid+1
    return res


arr=[1,3,4,13,13,14,14,14,15,15,18,19,20]
target=14
print(occur(arr,target))