#Search element through binary
def search(arr,target):
   start=0
   end=len(arr)-1
   res=-1
   while start<=end:
      mid=(start+end)//2
      if arr[mid]==target:
         return mid
      elif arr[mid]<target:
         start=mid+1
      else:
         res=mid
         end=mid-1
   return res
   
       


arr=[1,4,5,7,9,11,12,17,19]
target=20

print(search(arr,target))