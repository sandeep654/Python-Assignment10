#Write a python script to print first M multiples of N.
n=int(input("Enter n number:"))
for i in range(n*10,n-1,-n):
    print(i)
    i+=1 