#count number of rotation in arry
def rotate(arr):
    start=0
    end=len(arr)-1
    while start<end:
        mid=(start+end)//2
        if arr[start]<arr[mid]:
            res=start
            start=mid
        else:
            res=mid
            end=mid
    return res+1


arr=[122,123,124,125,134,136,145,167,183,56,76,87,98,102,103,119]
print(rotate(arr))