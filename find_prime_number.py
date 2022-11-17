"""Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45"""
for e in range(15,45+1):
    if e>1:
        for i in range(2,e):
            if(e%i)==0:
                break
        else:
            print(e)