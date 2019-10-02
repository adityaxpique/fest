num=int(input("Enter the number: "))
sum=0
temp=num
while(num>0):
    x=num%10
    num=int(num/10)
    q=(x*x*x)
    sum=sum+q

if(sum==temp):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
