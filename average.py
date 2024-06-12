#find average using for loop
number=[10,20,30,40,50]
sum=0
for i  in number:
    sum+=i
no=len(number)
average=sum/no
print("the average is",average)