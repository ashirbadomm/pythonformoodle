str1=input("Enter a string: ")
sub =input("Enter the substring: ")
index = 0
count= 0
while index < len(str1):        
    index = str1.find(sub, index)     
    if index == -1:        
        break
    print ("%s found at %d" % (sub , index+1))
    index += len(sub)
    count+=1
print ("Total count = %d" % count)
