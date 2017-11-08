print ("Zeller's Algorithm") 
print("Enter Your Day Value") 
B=int(input()) 
print("Enter Your Month Value") 
A=int(input()) 
print("Enter Your Year Value") 
C=int(input()) 
print("Enter Your Century Value") 
D=int(input()) 

W=(13*A-1)/5 
X=C/4 
Y=D/4 
Z=W + X + Y + B + C - 2 * D 
R=int(Z % 7) 

if R==0: 
    print ('Sunday') 
elif R==1: 
    print ('Monday') 
elif R==2: 
    print ('Tuesday') 
elif R==3: 
    print ('Wednesday') 
elif R==4: 
    print ('Thursday') 
elif R==5: 
    print ('Friday') 
elif R==6: 
    print ('Saturday') 
