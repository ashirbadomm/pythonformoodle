import math
class Time:
    hours=0
    minutes=0
    seconds=0
    def __init__(self):
        self.hours=0
        self.minutes=0
        self.seconds=0
    def get_values(self):
        self.hours=int(input("Enter hours "))
        self.minutes=int(input("Enter minutes "))
        self.seconds=int(input("Enter seconds "))
    
    def print_values(self):
        print ("Hours:",self.hours,": Minutes:", self.minutes,"Seconds:",self.seconds) 
    def __add__(self,other):
        d = Time()
        d.hours = self.hours + other.hours
        d.minutes = self.minutes + other.minutes
        if(d.minutes>=60): 
             d.minutes-=60
             d.hours+=1
        d.seconds = self.seconds + other.seconds
        if(d.seconds>=60):
            d.seconds-=60
            d.minutes+=1
            if(d.minutes==60):
                d.minutes-=60
                d.hours+=1
        d.hours=int(d.hours)
        d.minutes=int(d.minutes)
        d.seconds=int(d.seconds)
        return d
    
    def __sub__(self,other):
        d=Time()
        h1,m1,s1 = self.hours, self.minutes , self.seconds 
        h2,m2,s2 = other.hours , other.minutes , other.seconds
        t1 = s1*60*60 + m1*60 + h1
        t2 = s2*60*60 + m2*60 + h2
        t3 = math.fabs(t1-t2)
        h3 = t3%60
        m3 = (t3/60) % 60
        s3 = ((t3/60)/60) % 60
        d.hours , d.minutes , d.seconds = int(h3) , int(m3) , int(s3)
        return d
t1 = Time()
t1.get_values()
t2= Time()
t2.get_values()
t3 = t1 + t2
t3.print_values()
t4 = t1 - t2
t4.print_values()
