def smallest(arr,n):
  max=arr[0]
  for i in range(1,n):
    if arr[i] < max:
      max=arr[i]
  return max









print ("these are the values from the ⏱")
arr = [10,324,45,90,980,40,78,567,3]
n = len(arr)
Ans1 = largest(arr,n)
Ans2 = smallest(arr,n)
Ans3 = lar(arr,n)
Ans4 = min1(arr,n)
print ("largest given in array is ", Ans1)
print("smallest in given array is ",Ans2)
print ("largest given in array is ", Ans3)
print("smallest in given array is ",Ans4)