# write a python scipt to print first N odd natural number.
'''a=int(input("enter a number"))
i=1
while i<=a:
    print(i)
    i+=2
'''

a=int(input("enter a number"))
i=1
while i<=a:
    if i%2 ==1:
        print(i)
    i+=1
