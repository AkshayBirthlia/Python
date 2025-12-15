count = 0
num = int(input("Enter number here : "))
for i in range(1, num+1):
    if num%i == 0 :
        count += 1

if count == 2 :
    print("this is prime number ")
else :
    print("this is not a prime number ")