factorial = int(input("Enter factorial here : "))
sum = 1
for i in range(factorial  ,1,-1) :
    sum = i * sum

print("factorial ",sum)