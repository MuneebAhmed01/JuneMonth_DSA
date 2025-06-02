def search(arr,target):
   start=0
   end=len(arr)-1
   res=-1
   while start<=end:
      mid=(start+end)//2
      if arr[mid]==target:
         return f"THe floor is {arr[mid]} and ceil is {arr[mid]}"
      elif arr[mid]<target:
         start=mid+1
      else:
         res=mid
         end=mid-1
   return f"THe floor is {arr[res-1]} and ceil is {arr[res]}"
   
       


arr=[2,4,5,7,9,11,17,19]
target=1

print(search(arr,target))