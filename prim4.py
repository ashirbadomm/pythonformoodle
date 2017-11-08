s= int(input("enter size"))
for i in range(s):
    for j in range(2*i):
        print("\\",end="")
    for k in range (4*s-(4*i)-2):
        print ("!",end="")
    for l in range (2*i):
        print("/",end="")
    print("")
