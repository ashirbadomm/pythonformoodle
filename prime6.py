def validate_number(n):
    s=n
    sum1=0
    if len(s) == 16:
    
        for x in range(16):
            new=int(s[x])
            if x % 2 ==0:
                new=new*2
                if new >=10:
                    sum1=sum1+int(new/10)
                    sum1=sum1+int(new%10)
                else:
                    sum1=sum1+new
            else:
                 sum1=sum1+new
        print(sum1)
        if sum1 % 10 ==0:
            print("valid!!",sum1)
        else:
            print("invalid!!")

num=input("enter the number")
validate_number(num)
