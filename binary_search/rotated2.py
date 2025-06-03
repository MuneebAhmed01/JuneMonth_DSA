def rotate(arr,target):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return True
        if arr[start]==arr[mid] or arr[mid]==arr[end]:
            if arr[start]==arr[mid]:
                 start=start+1
            if arr[mid]==arr[end]:
                end=end-1
        
        if arr[start]>=arr[mid]:
            if arr[mid]<target<=arr[end]:
                start=mid+1
            else:
                end=mid-1
        else:
            
            if arr[start]<=target<arr[mid]:
                end=mid-1
            else:
                start=mid+1

    return False
                


    



arr = [4,5,6,7,0,1,2]
target = 0







print(rotate(arr,target))