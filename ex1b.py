user_list=[]
check="y"
while check=="y":
    user_tuple=()
    n=int(input("enter the tuple numbers or [end]"))
    while n !="end":
        user_tuple += (int(n),)
        n=(input("enter the tuple numbers or [end]"))
    user_list.append(user_tuple)
    check=input("want to add more tuples??(y) or (n)")
print("list before is",user_list)
def sort_tuple( lt ):
    dic={}
    for x in lt:
       dic[x[-1]]=x
    key=sorted(dic)
    sorted_user_list=[]
    for x in range(len(dic)):
        sorted_user_list.append(dic[key[x]])
    print("sorted is",sorted_user_list)
sort_tuple(user_list)