def conlist(namelist):
    for i in range(0,len(namelist)):
       dummydict={}
       temp={}
       for j in range(0,len(namelist)):
           if namelist[i] != namelist[j]:
               print("enter the rating for",namelist[j],"from",namelist[i]);
               temp = {namelist[j]: int(input(""))};
       dummydict.update(temp)
       temp={}
       dictlist.append(dummydict)

def maxRating(namelist,dictlist):
    for i in range(0,len(namelist)):
                temp = [[k,v] for k,v in dictlist[i].items()]
                for [key,value] in temp:
                          ratinglist[namelist.index(key)]+=value
    max1=""
    maxCount=0
    for i in range(0,len(namelist)):
            if maxCount<ratinglist[i]:
                maxCount=ratinglist[i]
                max1=namelist[i]
    if max1: return max1
    else: return "Everyone is the same" 

namelist=[]
dictlist=[]
ratinglist=[]
n=int(input("Enter the number of people? "))
for i in range(0,n):
    name=input("Enter name ")
    namelist.append(name)
    ratinglist.append(0)
conlist(namelist)
max1 = maxRating(namelist,dictlist)
print ("Most popular friend is: " ,max1)
