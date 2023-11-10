# Pyramid of numbers from 1 to 20 
sn = 1
n = int(input("Enter the number of rows:" ))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end ="")
    for j in range(i+1):
        print(sn,end =" ")
        sn += 1
    print()


    