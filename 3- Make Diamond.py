n = eval(input("please enter diamond's height:"))

for i in range(n):
    print(" "*(n-i), "*"*(i*2+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i), "*"*(i*2+1))