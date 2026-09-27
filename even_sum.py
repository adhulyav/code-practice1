num = int(input("Enter the positive number:"))
sum=0
count=0
for i in range(1,num+1):
  if i%2==0:
     sum+=i
     count+=1
     print(i)
print("the sum of even numbers:",sum)
print("nubmer of even numbers:",count)

