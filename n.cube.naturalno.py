#Write a python script to print cubes of first N natural numbers.
n=int(input("Enter n cube no. :"))
for e in range(1,n+1,1):
    print(e,",",e**3)