#WAP to print all positive number in a arnge
list=[8,4,-6,2,-4,9]
for num in list:
                if num>=0:
                print(num,end="")
                


#WAP ro print fibonacci series
num=int(input("Enter the number = "))
x=0
y=1
sum=0
count=1
print("Fibonacci series=",end="")
while(count<=num):
                  print(sum,end="")
                  count=count+1
                  x=y
                  y=sum
                  sum=x+y
