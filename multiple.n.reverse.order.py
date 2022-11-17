#Write a python script to print the first 10 multiples of N in reverse order.
n=int(input("Enter n number:"))
for i in range(n,n*11,n):
    print(i)
    i+=1 