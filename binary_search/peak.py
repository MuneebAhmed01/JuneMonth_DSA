#find peak element
#THis has error in edge cases but solved withour using gpt etc anything,Watch solution on leetcode for passing all edge cases
def peak(arr):
    start=0
    end=len(arr)-1
    if len(arr)==1:
        return arr[0]
    if arr[start]>arr[start+1]:
            return arr[start]
    if arr[end]>arr[end-1]:
            return arr[end]
    
    while start<=end:
        mid=(start+end)//2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return arr[mid]
        if start<mid:
            start=mid+1
        else:
            end=mid-1
   
arr=[1, 3, 5, 4, 2]
print(peak(arr))