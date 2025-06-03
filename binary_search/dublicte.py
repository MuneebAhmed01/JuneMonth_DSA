def dublicate(arr):
    start=0
    end=len(arr)-1
    target=-1
    while start<end:
        mid=(start+end)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            target=arr[mid]
        if arr[start]==arr[start+1] or arr[end]==arr[end-1]:
            if arr[start]==arr[start+1]:
                start+=1
            if arr[end]==arr[end-1]:
                end-=1
            continue
    return target
            



arr=[1,2,2,3,4,4,5,5,5,5,5]
print(dublicate(arr))