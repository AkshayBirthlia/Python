#even number looping
print("Enter how many even numbers you want to print: ")
n = int(input())
for i in range(1,n*2 + 1):
    if i % 2 == 0 :
        print(i)
    
