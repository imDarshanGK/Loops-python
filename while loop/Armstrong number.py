#program to check Armstrong number or not

n=int(input("Enter a number: "))
m=n
s=0
while n!=0:
    ud=n%10
    s=s+ud*ud*ud
    n=n//10
print("Sum=",s)

if m==s:
    print("It is a Armstrong number")
else:
    print("It is not a Armstrong number")
