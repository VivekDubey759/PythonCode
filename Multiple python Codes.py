#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


#Finding Adjacent Nodes
def num(a,b,c):
    return a[b][c]==1
num([
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
],0,1)


# In[7]:


#Virtual DAC
def num(a):
    return round(5*a/1023, 2)
num(400)


# In[11]:


#Drunken Python
def num(a):
    if type(a)==int:
        return str(a)
    else:
        return int(a)
num('374832')


# In[21]:


#Right Shift by Division
import math
def num(a,b):
    c=pow(2,b)
    d=a/c
    return math.floor(d)
num(-512, 10)


# In[25]:


#Find the Highest Integer in the List Using Recursion
def num(a):
    b=max(a)
    return b
num([8,4,2,5,67,69])


# In[35]:


#Length of Number
def num(a):
    b=list(str(a))
    c=[i for i in range(len(b))]
    d=c[-1]
    return d+1
num(0)


# In[43]:


#FizzBuzz Interview Question
def num(a):
    if a%3==0 and a%5==0:
        return "FizzBuzz"
    elif(a%3==0):
        return "Fizz"
    elif(a%5==0):
        return "Buzz"
    else:
        return str(a)
num(0)


# In[48]:


#Geometry 1: Length of Line Segment
def num(a,b):
    c=a[0]-b[0]
    d=a[1]-b[1]
    e=c*c
    f=d*d
    h=e+f
    g=pow(h,.5)
    return round(g,2)
num([0,0], [1,1])
    
    


# In[54]:


#Sum of Odd and Even Numbers
def num(a):
    b=sum([i for i in a if i%2==0])
    c=sum([i for i in a if i%2!=0])
    d=[b,c]
    return d
num([0, 0])


# In[70]:


#Cricket Balls to Overs!
def num(a):
    if a%6==0:
        b=a/6
        return b
    else:
        b=a%6
        c=a//6
        d=b*.1+c
        return d
num(2400)


# In[301]:


#Burglary Series (03): Is It Gone?
def num(a):
    b=list(a.keys())
    if 'timmy' in b:
        return "Timmy is gone..."
    else:
        return "Timmy is here!"
num({ })


# In[79]:


#A Circle and Two Squares
def num(a):
    b=2*a*a
    return b
num(7)


# In[95]:


#Get Students with Names and Top Notes
def num(a):
    b=list(a.values())
    c=[max(b[-1])]
    d=list(a.keys())
    e='top_note'
    f=d[0]
    g=[f,e]
    h=[b[0]]+c
    l=dict(zip(g,h))
    return l
num({ "name": "Zygmund", "notes": [1, 2, 3] })


# In[108]:


#Calculate the Profit
def num(a):
    b=list(a.values())
    c=list(a.keys())
    d=b[1]*b[-1]
    e=b[0]*b[-1]
    return d-e
num({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
})


# In[4]:


#Get the Area of a Country
def num(a,b):
    c=round(((b/148940000)*100),2)
    return a+" is "+str(c)+"%"+" of the total world's landmass"
num("Iran", 1648195)


# In[12]:


#Next Number Greater Than A and B and Divisible by B
def num(a,b):
    c=a%b
    d=b-c
    return d+a
num(17,8)


# In[18]:


#How Many Solutions Does This Quadratic Have?
def num(a,b,c):
    if (b*b)-(4*a*c)>0:
        return 2
    elif (b*b-4*a*c)==0:
        return 1
    else:
        return 0
num(1, 0, 0)


# In[29]:


#Date Format
def num(a):
    b=a.split('/')
    c=b[::-1]
    d="".join(c)
    return d
num('01/15/2019')


# In[35]:


#Adding Numbers
def num(a,b):
    if a=='' or b=='':
        return "Invalid Operation"
    else:
        return str(int(a)+int(b))
num("", "20")
    


# In[38]:


#List of Multiples
def num(a,b):
    c=[i*a for i in range(1,b+1) ]
    return c
num(17, 6)


# In[42]:


#Quadratic Equation
def num(a,b,c):
    return ((b**2-4*a*c)**0.5-b)/2/a
num(1, -12, -28)


# In[51]:


#Simple OOP Calculator
def num(a,b,c):
    if a=='+':
        return b+c
    elif(a=='-'):
        return b-c
    elif(a=='*'):
        return b*c
    else:
        return b//c
num('-',10, 5)
    


# In[55]:


#Return the Time Saved by Speeding
def num(a, b, c):
    return round((c/a - c/b)*60, 1)
num(80, 100, 10)


# In[62]:


#Hex to Binary
def num(a):
    b=bin(a)
    c=b[2:]
    return c
num(0xFF)


# In[65]:


#Invert Keys and Values
def num(a):
    b=list(a.keys())
    c=list(a.values())
    d=dict(zip(c,b))
    return d
num({ "zebra": "koala", "horse": "camel" })


# In[67]:


#Classes For Fetching Information on a Sports Player
class Football:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    def get_height(self):
        return f"{self.name} is {self.height} cm tall"
    def get_weight(self):
        return f"{self.name} weighs {self.weight} kg"
player1=Football('David Jones',25, 175, 75)
print(player1.get_age())
print(player1.get_height())
print(player1.get_weight())


# In[84]:


#String Pairs
def num(a):
    b=[a[i:i+2] for i in range(0,len(a),2)]
    return b
num("airforces")


# In[90]:


#Check If Lines Are Parallel
def num(a,b):
    c=(a[0]/a[1])*-1
    d=(b[0]/b[1])*-1
    return c==d
num([0, 1, 5], [0, 1, 5])


# In[93]:


#Fullname and Email
class Employee:
     def __init__(self, firstname, lastname):
            self.firstname=firstname
            self.lastname=lastname
            self.fullname = firstname + ' ' + lastname
            self.email=(firstname+"."+lastname+"@company.com").lower()
            
employee1 = Employee("John", "Doe")
print(employee1.fullname) 
print(employee1.email)
print(employee1.firstname)
print(employee1.lastname)
            


# In[95]:


#Two Distinct Elements
def num(a):
    b=[i for i in a if a.count(i)==1]
    return b
num([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])


# In[109]:


#Algebra Sequence — Boxes
def num(a):
    b=list(range(1,a+1))
    c=len([i for i in b if i%2==0])
    d=len([i for i in b if i%2!=0])
    if a==0:
        return 0
    elif(a%2==0 or a%2!=0):
        return d*3-c
    else:
        return 0
num(6)


# In[114]:


#Stupid Addition
def num(a,b):
    if type(a)==int and type(b)==int:
        return str(a)+str(b)
    elif(type(a)==str and type(b)==str):
        return int(a)+int(b)
    else:
        return 'None'
num(1,'2')


# In[124]:


#Sum Fractions
def num(a):
    b=sum(a,[])
    c=b[0::2]
    d=b[1::2]
    e=[i/j for i,j in zip(c,d)]
    return round(sum(e))
num([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]])


# In[140]:


#Characters and ASCII Code Dictionary
def num(a):
    if a==[]:
        return []
    else:
        b=[ord(i) for i in a]
        c=dict(zip(a,b))
        d=[{k: v} for k, v in c.items()]
        return d
    
num(["a", "b", "c"])


# In[141]:


#Ones, Threes and Nines (Version #1)
class number:
    def __init__(self,num):
        self.ones = num//1
        self.threes = num//3
        self.nines = num//9
num=number(5)
print(num.ones)
print(num.threes)
print(num.nines)
    


# In[147]:


#Algorithms I: Introduction to Recursion
import math
def num(a):
    b=math.factorial(a)
    return b
num(8)


# In[161]:


#Algorithms I: Introduction to Recursion
def num(a):
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
num(19)


# In[175]:


#Designing Rugs
def num(a,b,c):
    d=(c*b+"/")*a
    e=d.split('/')
    return e[0:-1]
num(2, 2, 'A')


# In[179]:


#Designing Rugs
def num(a,b,c):
    d=[c*b]*a
    return d
num(3, 5, '#')


# In[190]:


#Volume of a Spherical Shell
def num(a,b):
    b=(4/3)*(22/7)*((a*a*a)-(b*b*b))
    return abs(round(b,4))
num(3,800)


# In[195]:


#Burglary Series (06): Convert to Number
def num(a):
    b=list(a.values())
    c=list(a.keys())
    d=[int(i) for i in b]
    return dict(zip(c,d))
num({ "piano": "200", "tv": "300", "stereo": "400" })


# In[202]:


#CAPS LOCK DAY is over!
def num(a):
    if 'CAPS LOCK DAY' in a:
        b=a.capitalize()+'!'
        return b
    else:
        b= a.capitalize()
        return b
num("Let us stay calm, no need to panic.")


# In[210]:


#Which Function Returns the Larger Number?
def num(a,b):
    if a()>b():
        return 'a'
    elif(a()<b()):
        return 'b'
    else:
        return 'neither'
num(lambda: 505050, lambda: 5050)
    


# In[236]:


#Robot Path
def num(a):
    Destination1= ['e','n','e','e','n']
    Destination2=['w','n','w','n','w','w','n']
    b=a.count('n')
    c=a.count('s')
    d=a.count('e')
    e=a.count('w')
    f=b-c
    g=e-d
    h=d-e
    if (h==3 and f==2):
        return True
    elif(f==3 and g==4):
        return True
    else:
        return False
num(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"])
    
    


# In[254]:


#Last Digit Ultimate
def num(a,b,c):
    d=list(str(a))
    e=list(str(b))
    f=list(str(c))
    g=int(d[-1])
    h=int(e[-1])
    i=int(f[-1])
    k=list(str(g*h))
    l=int(k[-1])
    return l==i
num(12, 215, 2142)


# In[278]:


#Face Interval
def num(a):
    if type(a)==str:
        return ":/"
    elif (type(a)==list):
        b=max(a)
        c=min(a)
        d=b-c
        if d in a:
            return ":)"
        else:
            return ":("
num([1, 2, 5, 8, 3, 9])


# In[288]:


#All Occurrences of an Element in a List
def num(a,b):
    c=[i for i in range(len(a)) if a[i]==b ]
    return c
num(["a", "a", "b", "a", "b", "a"], "a") 


# In[314]:


#International Greetings
def num(a):
    b = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
    c=list(b.keys())
    d=list(b.values())
    if a in c:
        if a =='Randy':
            return "Hi! I'm Randy, and I'm from Germany."
        elif (a=='Karla' ):
            return "Hi! I'm Sam, and I'm from France."
        elif(a=='Wendy'):
            return "Hi! I'm Wendy, and I'm from Japan."
        elif(a=='Norman'):
            return "Hi! I'm Norman, and I'm from England."
        elif(a=='Sam'):
            return "Hi! I'm Sam, and I'm from Argentina."
    else:
        return "Hi! I'm a guest."
    
num('Moti')


# In[325]:


#Incorrect Import Statement
def num(a):
    b=a.split(' ')
    c=b[1]
    d=b[-1]
    return "from"+" "+d+" "+'import'+' '+c
num("import pi from math")


# In[335]:


#Name Classes
class Name:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.fullname=fname+" "+lname
        self.intials=fname[0]+"."+lname[0]
nameclass=Name("john", "SMITH")
print(nameclass.fullname)
print(nameclass.intials)
print(nameclass.fname)
print(nameclass.lname)


# In[348]:


#Find the Vertex of a Quadratic
def num(a,b,c):
    d=-b/(2*a)
    e=a*d**2 + b*d + c
    return [d,e]
num(1, 10, 4)


# In[361]:


#All About Lambda Expressions: Adding
def num(a):
    x=lambda a:a+10
    print(x(4))
num(4)


# In[385]:


#Validate Pin
def num(a):
    if len(a)==4 or len(a)==6:
        if a.isnumeric():
            return True
        else:
            return False
    else:
        return False
num('4983')
        


# In[390]:


#Harmonic Series
def num(a):
    b=round(sum([1/i for i in range(1,a+1)]),3)
    return b
num(10)


# In[396]:


#Transcribe to mRNA
def num(a):
    mapping = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([mapping[c] for c in a])
num("CGATATA")


# In[405]:


#Change Every Letter to the Next Letter
def num(a):
    b=list(a)
    c=[ord(i) for i in b]
    d="".join([chr(i+1) for i in c])
    return d
num("welcome")


# In[416]:


#Harshad Number
def num(a):
    b=list(str(a))
    c=sum([int(i) for i in b])
    if a%c==0:
        return True
    else:
        return False
num(200)


# In[436]:


#Stalactites or Stalagmites?
def num(a):
    if 1 in (a[0]) and 1 in (a[-1]):
        return "both"
    elif 1 in a[-1]:
        return "stalagmites"
    else:
        return "stalactites"
num([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])


# In[438]:


#New Word Builder
def num(a, b):
    return ''.join(a[i] for i in b)
num(["e", "t", "s", "t"], [3, 0, 2, 1])


# In[449]:


#Concatenate Variable Number of Input Lists
def num(*args):
    b=[i for i in args]
    c=sum(b,[])
    return c
num([4, 4, 4, 4, 4])


# In[454]:


#A Long Long Time
def num(a,b,c):
    d=60*60*a
    e=60*b
    if d>c and d>e:
        return a
    elif( e>d and e>c):
        return b
    else:
        return c
num(15, 955, 59400)


# In[457]:


#Emphasise the Words
def num(a):
    b=a.title()
    return b
num("GOOD MORNING")


# In[491]:


#Emphasise the Words
def num(a):
    b=a.lower()
    c=b.split(' ')
    d=[i[0].upper() for i in c]
    e=[i[1:] for i in c]
    f=[i+j for i,j in zip(d,e)]
    return " ".join(f)
num('GOOD MORNING')


# In[499]:


#Sastry Numbers
def num(a):
    b=str(a+1)
    c=int(str(a)+b)
    d=pow(c,.5)
    if int(d)==d:
        return True
    else:
        return False
num(1067551)
    


# In[505]:


#Sum of v0w3ls
def num(a):
    b=a.lower()
    c={'A':4,'E':3,'I':1,'O':0,'U':0}
    c=[i for i in b if i in"aeiouAEIOU"]
    d=c.count('e')*3
    e=c.count('i')
    f=c.count('a')*4
    g=d+e+f
    return g
num("I love edabit!")
       
    


# In[508]:


#List Multiplier
def num(a):
    b=len(a)
    c=[[i]*b for i in a]
    return c
num(["A", "B", "C", "D", "E"])


# In[550]:


#Intersecting Intervals
def num(a,b):
    c=sum(a,[])
    return d
    d=c[1::2]
    e=[i for i in d if i>=b]
    if e==[] and c[-1]==b:
        return len(e)+1
    else:
        return len(e)
num([[1, 2], [5, 6], [5, 7]], 3)


# In[555]:


#Pandigital Numbers
def num(a):
    b=list(set(str(a)))
    if len(b)==10:
        return True
    else:
        return False
num(112233445566778899)


# In[560]:


#Wash Your Hands :)
def num(N, nM):
    a = N*21*nM*30
    return '{} minutes and {} seconds'.format(a//60, a%60)
num(7,8)


# In[564]:


#Oddish vs. Evenish
def num(a):
    b=list(str(a))
    c=sum([int(i) for i in b])
    if (c%2==0):
        return 'Evenish'
    else:
        return 'Oddish'
num(4433)
    


# In[577]:


#Is the Number a Repdigit
def num(a):
    if a>=0:
        b=str(a)
        c=int(b[::-1])
        return a==c
    else:
        return False
num(77)


# In[583]:


#Is the Number a Repdigit
def num(a):
    b=set(str(a))
    return len(b)==1
num(99)
    


# In[586]:


#Letters Shared Between Two Words
def num(a,b):
    c=[i for i in a if i in b]
    d=len(c)
    return d
num("spout", "shout")
    


# In[598]:


#Is Johnny Making Progress?
def num(a):
    b=0
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            b+=1
    return b
num([10, 11, 12, 9, 10])


# In[608]:


#Is Johnny Making Progress?
def num(a):
    b=[x>y for (x,y) in zip(a[1:],a[:-1])]
    return b
num([3, 4, 1, 2])


# In[624]:


#Perfect Square Patch
def num(a):
    b=str(a)
    c=list(b*a)
    d=[[i]*a for i in c]
    return d
num(5)


# In[660]:


#Number of Lists in a List
def num(a):
    b=list(str(a))
    c=b.count('[')
    return c-1
num([1, 2, 3])


# In[671]:


#Reverse Words in a String
def num(a):
    b=a.strip()
    c=b.split(' ')
    d=c[::-1]
    return " ".join(d)
num("a good   example")


# In[684]:


#Combinatorial Exploration
def num(a):
    b=1
    for i in range(1,a+1):
        b=(b*i)
    c=len(str(b))
    return c
num(8)


# In[20]:


#Fruit Juices
def num(a,b):
    c=a.upper()
    e=c.split(' ')
    k="".join([i[0:3] for i in e])
    d=''.join([i for i in b if i in '0123456789'])
    return k+d
num("passion fruit", "750ml")


# In[32]:


#Impossible Date
from datetime import datetime
def num(day, month, year):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False
num(89, 3, 2020)


# In[48]:


#Get Student Top Notes
def num(a):
    
    if 'notes' in a[0] :
        b=[ i['notes'] for i in a ]
        c=[max(i) for i in b]
        return c
    else:
        return 0
num([
  {
    "id": 1,
    "name": "Jacek"
  },
  {
    "id": 2,
    "name": "Ewa"
  },
  {
    "id": 3,
    "name": "Zygmunt"
  }
])


# In[5]:


#Basic Statistics: Median
import statistics 
def num(a):
    b=statistics.median(a)
    return b
num([1, 2, 4, 5, 6, 8, 8, 8, 10])


# In[14]:


#Reversing a Binary String
def num(a):
    b=bin(a)
    c=b[2:]
    d=c[::-1]
    return int(d,2)
num(45)


# In[5]:


#Digit Distance
def num(a,b):
    c=list(str(a))
    d=list(str(b))
    e=[int(i) for i in c]
    f=[int(i) for i in d]
    g=sum([(i-j) for i,j in zip(f,e)])
    return g
num(10, 20)
    


# In[11]:


#Peeling off the Outer Layers
def num(a):
    b=[i[1:-1] for i in a[1:-1]]
    return b
num([
  ["hello", "world"],
  ["hello", "world"]
])


# In[45]:


#Construct and Deconstruct
def num(a):
    b=[a[:i] for i in range(1,len(a)+1)]+ [a[:-i] for i in range(1,len(a))]
    return b
num('hello')


# In[63]:


#Sum of Missing Numbers
def num(a):
    b=sorted(a)
    c=list(range(b[0],b[-1]+1))
    d=[i for i in c if i not in b]
    return sum(d)
num([10, 7, 5, 3, 1])


# In[64]:


#Returning an "Add" Function
def num(a):
    x=lambda n: a+n
    print(x(20))
num(5)


# In[72]:


#Extending The String
def num(a):
    b=[i for i in a if i in 'aeiouAEIOU']
    return len(b)
num('Smithsonian')


# In[71]:


#Extending The String
def num(a):
    b=a.lower()
    c=[i for i in b if i in 'bcdfghjklmnpqrstvwxyz']
    return len(c)
num('Smithsonian')


# In[92]:


#Numbered Cards
def num(a,b):
    c=sorted(a)
    d=sorted(b)
    e=c[-2:]
    f=int("".join([str(i) for i in e])[::-1])
    g=d[-2:]
    h=int("".join([str(i) for i in g])[::-1])
    if (f>h):
        return True
    elif(f<h):
        return False
    else:
        return False
num([1, 2, 3, 4, 5], [9, 8, 7, 6, 5])


# In[115]:


#Abbreviating a Sentence
def num(a,b):
    c=a.split(' ')
    d=[i for i in c if len(i)>b]
    e=[i.upper() for i in d]
    f=[i[0] for i in e]
    g="".join(f)
    return g
num("do it yourself", 2)


# In[123]:


#Abbreviating a Sentence
def num(a,b):
    c=a.split(' ')
    d=[i for i in c if len(i)>=b]
    e=[i.upper() for i in d]
    f=[i[0] for i in e]
    g="".join(f)
    return g
num("the acronym of long word lengths",5)


# In[130]:


#Rectangle in Circle
def num(a,b,c):
    d=(a*a)+(b*b)
    f=pow(d,(.5))
    e=2*c
    return f<=e
num(4, 7, 4)


# In[133]:


#Free Throw Probability
def free_throws(success, rows):
    success = int(success.strip('%')) / 100
    result = str(round(success ** rows * 100)) + '%'
    return result
free_throws("75%", 5)


# In[147]:


#Consecutive Numbers
def num(a):
    b=sorted(a)
    c=list(range(b[0],b[-1]+1))
    if b==c:
        return True
    else:
        return False

num([5, 1, 4, 3, 2])


# In[32]:


#Palindromic Dates
def num(a):
    b=a.split("/")
    f="".join(b)
    c=f[::-1]
    d=b[1]+b[0]+b[2]
    e=d[::-1]
    return f==c and d==e
    
num("11/02/2011")


# In[43]:


#Capitalize the Last Letter
def num(a):
    b=a.split(' ')
    c=[i[-1].upper() for i in b]
    d=[i[0:-1] for i in b]
    e=[(i+j) for i,j in zip(d,c)]
    return ' '.join(e)
num("HELp THe LASt LETTERs CAPITALISe")


# In[64]:


#Is This a Right Angled Triangle?
def num(a,b,c):
    d=max(a,b,c)
    e=d*d
    f=min(a,b,c)
    g=f*f
    h=[a,b,c] 
    j=[d,f]
    l=[i for i in h if i not in j]
    m=l[0]
    n=m*m
    return e==g+n
num(3, 4, 7)


# In[96]:


#Sum of Every Nth Number
def num(a,b):
    c=a[b-1::b]
    return sum(c)
num([6, 8, 9, 4, 6, 4, 7, 1, 5, 6, 10, 2], 13)


# In[97]:


#Calculate the Shortest Distance Between Two Points
def num(a):
    b=a.split(",")
    d=[int(i) for i in b]
    e=(d[0]-d[2])**2
    f=(d[1]-d[3])**2
    g=(e+f)
    h=pow(g,(.5))
    return round(h,2)
num("-5,2,3,1")
    


# In[120]:


#Stretched Words
def num(a):
    b=set(a)
    c=[set(i) for i in a]
    return c
num('ppoeemm')


# In[132]:


#Does the Cargo Fit? (Part 1)
def num(a,b):
    b=[True if i=='S' and j<=50 else True if i=='M' and j<=100 else True if i=='L' and j<=200 else False for i,j in zip(a,b)]
    c=list(set(b))
    if c==[True]:
        return True
    else:
        return False
num(["L", "L", "M"], [56, 60, 84, 900])


# In[136]:


#Stretched Words
def num(a):
    return a[0] + ''.join(a[i] for i in range(1,len(a)) if a[i] != a[i-1])
num("wiiiinnnnd")


# In[137]:


def num(r, c):
    return [[min(i[0],j[0]),max(i[1],j[1])] for i,j in zip(r,c)]
num([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]])


# In[141]:


#Rock, Paper, Scissors
def num(a,b):
    if (a=='Rock' and b=='Scissors'):
        return 'The winner is p1'
    elif(a=='Scissors' and b=='Rock'):
        return 'The winner is p2'
    elif(a=='Scissors' and b=='Paper'):
         return 'The winner is p1'
    elif(a=='Paper' and b=='Scissors'):
         return 'The winner is p2'
    elif(a=='Paper' and b=='Rock'):
        return 'The winner is p1'
    elif(a=='Rock' and b=='Paper'):
        return 'The winner is p2'
    else:
        return "It's a draw"
num("Scissors", "Paper")


# In[150]:


#Find the Shared Letters between Two Strings
def num(a,b):
    a=a.lower()
    b=b.lower()
    c="".join(sorted([i for i in a if i in b]))
    return c
num("house", "villa")


# In[164]:


#From A to Z
def num(a):
    b=a.split("-")
    c=[ord(i) for i in b]
    d=list(range(c[0],c[-1]+1))
    e=[chr(i) for i in d]
    return "".join(e)
num("Q-Z")


# In[186]:


#Car Timer
def num(a):
    if a<60:
        b=list(str(a))
        c=sum([int(i) for i in b])
        return c
    else:
        b=a//60
        c=a%60
        d=str(b)+str(c)
        e=list(str(d))
        f=[int(i) for i in e]
        g=sum(f)
        return g
num(24)


# In[191]:


#Mini Sudoku
def num(a):
    b=sum(a,[])
    c=sorted(b)
    d=[1,2,3,4,5,6,7,8,9]
    if c==d:
        return True
    else:
        return False
    
num([[8, 9, 2], [5, 6, 1], [3, 7, 4]])


# In[205]:


#Reversible Inclusive List Ranges
def num(a,b):
    if a<b:
        c=list(range(a,b+1))
        return c
    else:
        d=[a,b][::-1]
        e=list(range(d[0],d[-1]+1))[::-1]
        return e
num(1,5)


# In[243]:


#Crowded Carriage Capacity
def num(a,b):
    c=a/len(b)
    for i in b:
        if i<=(c/2):
            d=b.index(i)
            return d
    else:
        return -1
num(200, [35, 23, 40, 21, 38])


# In[252]:


#Crowded Carriage Capacity
def num(a,b):
    c=a/len(b)
    b=[b.index(i) if  i<=(c/2) else -1 for i in b]
    f=[i for i in b if i>=0]
    if len(f)==0:
        return -1
    else:
        return f[0]
num(200, [35, 23, 18, 10, 40])


# In[267]:


#Subset Validation
def num(a,b):
    c=[]
    for i in a:
        if set(i).issubset(set(b)):
            c.append(i)
    if len(c)==len(a):
        return True
    else:
        return False
num([[1, 2, 3, 4]], [1, 2, 3])


# In[269]:


#Subset Validation
def num(a,b):
    return all(set(i).issubset(b) for i in a)
num([[1, 2, 3], [2], [3], []], [1, 2, 3])
    


# In[323]:


#Simple Circle Collision Detection
def num(a,b):
    c=(a[1]-b[1])**2
    d=(a[2]-b[2])**2
    e=c+d
    f=pow(e,(.5))
    g=a[0]+b[0]
    if f<=g:
        return True
    else:
        return False
num([10, 0, 0], [10, 10, 10])


# In[329]:


#Remove Repeated Letters
def num(a):
    c=[]
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            c.append(a[i])
    c.append(a[-1])
    return "".join(c)
num("nanannnana")
        


# In[364]:


#Extend the Vowels
def num(a,b):
    c=list(a)
    if b>=1:
        d="".join([i*b if i in 'aeiouAEIOU'else i for i in c])
        return d
    else:
        return a
num("Extend", 0)


# In[365]:


#Evaluating Factorials
import math
def num(a):
    b=[i.replace('!',"") for i in a]
    c=[int(i) for i in b]
    e=sum([math.factorial(i) for i in c])
    return e
num(["0!", "1!"])


# In[383]:


#Reverse the Odd Length Words
def num(a):
    b=a.split(' ')
    c=" ".join([i[::-1] if len(i)%2!=0 else i for i in b])
    return c
num('Make sure uoy only esrever sdrow of ddo length')


# In[384]:


#Finding Common Elements
def num(a,b):
    c=list(set([i for i in a if i in b]))
    return c
num([1, 2, 3, 4, 5], [10, 12, 13, 15])


# In[401]:


#Explosion Intensity
def num(a):
    if a%2==0 and a%5==0:
        return 'B'+'O'*a+'M'+"!"
    elif a<2:
        return 'boom'
    elif a%2==0:
        return 'B'+'o'*a+'m'+'!'
    else:
        return 'B'+'O'*a+'M'
num(10)


# In[489]:


#Balanced List
def num(a):
    b=int(len(a)/2)
    c=sum(a[0:b])
    d=sum(a[(b):])
    if c<d:
        e=a[(b):]
        f=[str(i) for i in e]*2
        g=[int(i) for i in f]
        return g
    elif (c>d):
        k=a[0:b]
        l=[str(i) for i in k]*2
        h=[int(i) for i in l]
        return h
    else:
        return a
num([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6])


# In[490]:


#Smiley Faces :)
def num(a):
    b=a.count(':)')
    c=a.count('(:')
    d=a.count(':(')
    e=a.count('):')
    return b*1+c*1+d*(-1)+e*(-1)
num("::::")
    


# In[491]:


#Circular Shift
def num(lst1, lst2, n):
    return lst1 == lst2[n:] + lst2[:n]
num([1, 1], [1, 1], 6)


# In[492]:


#Percentage Changed
def num(a,b):
    c=int(a.replace("$",""))
    d=int(b.replace("$",""))
    if c>d:
        e=((c-d)/c)*100
        return str(e)+"%"+' '+'decrease'
    else:
        f=((d-c)/c)*100
        return str(f)+"%"+' '+'increase'
    

num("$100", "$950")


# In[488]:


#First N Vowels
def num(a,b):
    c=[i for i in a if i in 'aeiouAEIOU']
    if len(c)>b:
        d=c[0:b]
        return "".join(d)
    else:
        return '-1'
num("hostess", 5)


# In[508]:


#Remove Repeated Characters
def num(a):
    b=list(dict.fromkeys(a))
    return "".join(b)
num("hello")


# In[514]:


#A Simple Task
def num(a):
    b=str(a)
    if '.' in b:
        c=b.split('.')
        d=[int(i) for i in c]
        e=float('0'+'.'+str(d[-1]))
        return e
    else:
        return 0
num(1991.96)


# In[519]:


#Coaxial Cable Impedance
import math
def num(a,b,c):
    d=138*(math.log10(a/b))/math.sqrt(c)
    return round (d,1)
num(4.48, 1.33, 2.2)


# In[532]:


#Letters Only
def num(a):
    b=a.replace(" ",'')
    if b.isalpha() and b.islower():
        return True
    else:
        return False
num("")


# In[563]:


#Making a Sandwich
def num(a,b): 
        if b in a:
            c=a.index(b)
            a.insert(c,'bread')
            a.insert(c+2,'bread')
            return a
        else:
            return False
num(["ham", "ham"], "ham")


# In[577]:


#Making a Sandwich
def num(a,b):
    c=[['bread',i,'bread'] if i==b else [i] for i in a]
    d=sum((i if isinstance(i, list) else [i] for i in c), [])
    return d
num(["tuna", "ham", "tomato"], "ham")


# In[565]:


#Making a Sandwich
def num(a,b):
    c=[['bread',i,'bread'] if i==b else [i] for i in a]
    d=sum(c,[])
    return d
num(["tuna", "ham", "tomato"], "ham")


# In[620]:


#Making a Sandwich
def num(a,b):
    c=''.join([' bread '+i+' bread ' if i==b else i for i in a]).split()
    return c
num(["tuna", "ham", "tomato"], "ham")


# In[623]:


#Adding Both Ends Together
def num(a):
    m=[i*-1 if i<0 else i for i in a]
    b=[str(i) for i in m]
    c=[i[0] for i in b]
    d=[i[-1] for i in b]
    e=[int(i) for i in c]
    f=[int(i) for i in d]
    g=[True if i+j==10 else False for i,j in zip(e,f)]
    k=g.count(True)
    return k
num([19, 46, 2098])


# In[709]:


#Collatz Conjecture
def num(a):
    b=[]
    while(a!=1):
        b.append(a)
        a=a*3+1 if a%2 else a//2
    return len(b)+1,max(b)
        
num(3)


# In[750]:


def collatz_sequence_length(n):
    steps = 0
    highest = n
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        
        steps += 1
        highest = max(highest, n)
    
    return steps, highest

collatz_sequence_length(10)


# In[759]:


#Union and Intersection of Lists
def num(a,b):
    c=[i for i in a if i in b]
    d=a+b
    e=sorted(list(dict.fromkeys(c)))
    f=sorted(list(dict.fromkeys(d)))
    if (list(set(a))==list(set(b))) and len(a)<len(b):
        return [f,f]
    elif list(set(a))==list(set(b)) and len(a)>len(b):
        return [f,f]
    else:
        return [e,f]
num([1, 2, 3, 4, 4], [4, 5, 9])


# In[760]:


#Replace Letters With Position In Alphabet
def num(a):
    b=[i for i in a if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    c=[ord(i)-64 if i.isupper() else ord(i)-96 for i in b]
    d=[str(i) for i in c]
    e=" ".join(d)
    return e
num("We have a lot of rain in June.")


# In[761]:


#Largest Gap
def num(a):
    b=sorted(a)
    c=[b[i+1]-b[i] for i in range(len(b)-1)]
    return max(c)
num([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9])


# In[762]:


#Joining Digits Together
def num(a):
    c=list(range(1,a+1))
    b=[list(str(i)) for i in c]
    d=sum(b,[])
    e='-'.join(d)
    return e
num(100)


# In[775]:


#House of Cards
def num(a):
    b=a*(3*a+1)/2
    return b
num(1)


# In[793]:


#Accumulating Product
import math
def num(a):
    curr=1
    d = [(curr:=curr*v) for v in a]
    return d
num([1, 5, 7])


# In[794]:


#GCD and LCM (Part 2)
def num(a,b):
    c=a*b
    d=list(range(1,c+1))
    e=[i for i in d if i%a==0 and i%b==0]
    f=min(e)
    return f
num(3,5)


# In[814]:


#Standard Deviation
import statistics
def num(a):
    b=statistics.stdev(a)
    return b
num([5, 5, 5])


# In[815]:


#Standard Deviation
import statistics
def num(a):
    b=len(a)
    c=sum(a)/b
    d=[abs(i-c) for i in a]
    e=sum([pow(i,2) for i in d])
    f=e/b
    h=pow(f,(.5))
    return round(h,2)
    
num([5, 5, 5])


# In[15]:


#Turn That Frown Upside Down
def num(a):
    b=a.replace(":(",':)')
    c=b.replace("8(",'8)')
    d=c.replace('x(','x)')
    e=d.replace(';(',';)')
    return e
num("print('x(')")


# In[16]:


#Power of Two
def num(a):
    return (a & (a - 1)) == 0
num(18)


# In[38]:


#The Fibonacci Number
def fibonacci(num):
    a, b = 1, 1
    for i in range(1, num):
        a, b = b, a+b
    return b
fibonacci(6)


# In[39]:


#The Fibonacci Number
def num(a):
    b,c=1,1
    for i in range(1,a):
        b,c=c,b+c
    return c
num(6)


# In[40]:


#Food for Everyone!
class Person:
    def __init__(self,hates,name,likes):
        self.hates=hates
        self.name=name
        self.likes=likes
        def taste(self,food):
            if food in self.likes: add = " and loves it"
            elif food in self.hates: add = " and hates it"
            else: add=""
            return self.name + " eats the " + food + add + "!"


# In[41]:


#Return Duplicate Numbers
def num(a):
    b=[i for i in a if a.count(i)>1]
    c=list(dict.fromkeys(b))
    if len(c)>0:
        return c
    else:
        return 'None'
num([1, 2, 3, 4, 3, 5, 6])


# In[42]:


#Case and Index Inverter
def num(a):
    b=a.swapcase()
    c=b[::-1]
    return c
num("XeLPMoC YTiReTXeD")


# In[43]:


#Mubashir's Mystery Challenge
def num(a,b):
    c = sum(int(i) for i in str(a))
    d = sum(int(j) for j in str(b))
    return c * d
num(10,10)


# In[45]:


#Mubashir's Mystery Challenge
def num(a,b):
    if a==0:
        return 0
    else:
        return b//a
num(0,1)


# In[51]:


#Broken Keyboard
def num(a,b):
    c=list(a)
    d=list(b)
    e=list(dict.fromkeys([i for i in c if i not in d]))
    return e
num("starry night", "starrq light")


# In[62]:


#Split Item Codes
def num(a):
    b=[int("".join([i for i in a if i in '0123456789']))]
    c=["".join([i for i in a if i not in '0123456789'])]
    d=c+b
    return d
num("SRPE5532")


# In[63]:


#The Empty Square Sequence
def num(a):
    b=4*a*(a-1)
    return b
num(10)


# In[66]:


#Tower of Hanoi
def num(a):
    b=pow(2,a)
    c=b-1
    return c
num(0)


# In[75]:


#Filtering by Star Rating
def num(a,b):
    c={k,v for (k,v) in a.items() if b in v}
    return c
num({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
},"*****")


# In[77]:


#Filtering by Star Rating
def num(a,b):
    c={k:v for (k,v) in a.items() if b in v}
    return c
num({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
},"*****")


# In[105]:


#Percentage of Box Filled In
def num(a):
    d=a[1:-1]
    e=''.join(d)
    f=e.count(' ')
    g=e.count('o')
    k=f+g
    h=round((g/k)*100)
    return str(h)+"%"
num([
  "######",
  "#ooo #",
  "#oo  #",
  "#    #",
  "#    #",
  "######"
])


# In[45]:


#Are They the Same?
def num(a,b,c):
    d={k:v for (k,v) in a.items() if c in k}
    e={k:v for (k,v) in b.items() if c in k}
    if d==e:
        return True
    if d=={} or e=={}:
        return "One's empty"
    else:
        return "Not the same"
num({ "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" },{ "people": 12, "sun": "star", "book": "bad" },"sun")


# In[46]:


#All Numbers in List Are Prime
def num(lst):
    x = [x for x in lst if x>1 and all(x%i for i in range(2, x))]
    return True if len(x) == len(lst) else False
num([1, 5, 3])


# In[47]:


#Sum of Digits Between Two Numbers
def num(a,b):
    c=list(range(a,b+1))
    d=[list(str(i)) for i in c]
    e=sum(d,[])
    f=sum([int(i) for i in e])
    return f
num(10,12)


# In[48]:


#Sum of Digits Between Two Numbers
def num(a,b):
    c=list(range(a,b+1))
    d=list("".join([str(i) for i in c]))
    e=sum([int(i) for i in d])
    return e
num(10,12)


# In[65]:


#Merge Lists in Order
def num(a,b):
    if a==sorted(a):
        return sorted(a+b)
    else:
        c=sorted(a+b)
        d=c[::-1]
        return d
num([120, 180, 200], [190, 175, 130])


# In[70]:


#Recursion: Count Vowels
def num(a):
    b=len([i for i in a if i in 'aeiouAEIOU'])
    return b
num("")


# In[80]:


#Mini Peaks
def num(a):
    #b=[a[i] if (a[i] > a[i-1] and a[i] > a[i+1]) else 'a' for i in range(len(a))]
    b=[a[i] if a[i]>a[i-1] and a[i]>a[i+1] else 'a' for i in range(len(a))]
    c=[i for i in b if i!='a']
    return c
num([4, 5, 2, 1, 4, 9, 7, 2])


# In[124]:


#Just Find the Vertex
def num(a):
    b=a.split(' ')
    d=b[0]
    e=''.join(b[1:3])
    f=int(d.replace("x",''))
    g=int(e.replace('x',''))
    h=-g/(2*f)
    
    return h
    
num("7x + 14x +28")


# In[132]:


#Just Find the Vertex
def num(a):
    b=a.split(' ')
    d=b[0]
    e=b[2]
    k=b[1]
    f=int(d.replace("x",''))
    g=int(e.replace('x',''))
    l=int(k+str(g))
    m=-l/(2*f)
    return m
    
num("-5x + 50x -120")


# In[142]:


#Poker Full House
def num(a):
    b=list(set(a)) 
    if len(b)==2 and (a.count(b[0])==2 and a.count(b[1])==3):
        return True
    elif (len(b)==2 and (a.count(b[0])==3 and a.count(b[1])==2)):
        return True
    else:
        return False
num(["7", "J", "3", "4", "2"])


# In[152]:


#String Match by Two Letters
def num(a,b):
    c=[a[i:i+2] for i in range(len(a))]
    d=[b[i:i+2] for i in range(len(b))]
    e=[i for i in c if len(i)==2]
    f=[i for i in d if len(i)==2]
    g=len([i==j for i,j in zip(e,f) if i==j])
    return g
num("", "")


# In[208]:


#Uno (Part 1)
def num(a,b):
    c=''.join(a)
    d=b.split(' ')
    if d[0] in c:
        return True
    elif d[1] in c:
        return True
    else:
        return False
num(["yellow 3", "pink 7"], "red 8")


# In[209]:


#Number of Leap Years
def num(a):
    b=a.split('-')
    c=[int(i) for i in b]
    d=list(range(c[0],c[-1]+1,4))
    e=[i for i in d if i%100==0]
    f=len([i for i in e if i%400==0])
    h=len(d)-len(e)+f
    return h
num("1980-1984")


# In[25]:


#Product of Two Largest Numbers
def num(a):
    b=list(set(a))
    if len(b)==1 and len(a)>1:
        return b[0]*b[0]
    else:
        c=max(a)
        d=[i for i in a if i!=c]
        e=max(d)
        return e*c
num([2, 3, 1, -1, 2])


# In[54]:


#Sum of Decimals
def num(a,b):
    c=a+b
    return c
num(1.234, 5.6789)


# In[12]:


#Slidey Numbers
def num(a):
    b=list(str(a))
    c=[int(i) for i in b]
    d= [i-j for i,j in zip(c,c[1:])]
    e=list(set([i==1 or i==-1 for i in d]))
    if e==[True]:
        return True
    else:
        return False
num(987654321)


# In[13]:


#Reverse Coding Challenge #1
def num(a):
    b=list(a)
    c=b[0::2]
    d=b[1::2]
    e=[int(i) for i in d]
    f=''.join([i*j for i,j in zip(c,e)])
    return f
num("A1B2C3D4")


# In[15]:


#A Redundant Function
def num(a):
    def func():
        return a
    return func
num('apple')


# In[50]:


#Let's Talk Like a Monkey 
def num(a):
    b=a.split(' ')
    c=['Eek' if i[0] in 'AEIOUaeiou' else 'Ook' for i in b]
    d=c[1:]
    e=[i.lower() for i in d]
    f=c[-1:]
    h=f+e
    return ' '.join(h)+"."
num("Mubashir Hassan")


# In[69]:


#Height of the Tallest Building
def num(a):
    b=len(a)
    c=sum('#' in i for i in a)
    d=str(c*20)+"m"
    return d
num([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
])


# In[91]:


#Height of the Tallest Building
def num(a):
    b = [item for item in a if "#" in item]
    return str(len(b) * 20) + "m"
num([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
])


# In[120]:


#Baseball Batting Average
def num(a):
    e=sum([i[0] for i in a])
    f=sum([i[1] for i in a])
    d=round(e/f,3)
    return d
num([[0, 0], [1, 3], [2, 2], [0, 4], [1, 5]])


# In[7]:


#Flash Cards
def num(a):
    if a[1]=="x":
        return a[0]*a[2]
    elif(a[1]=='+'):
        return a[0]+a[2]
    elif(a[1]=='-'):
        return a[0]-a[2]
    elif(a[2]==0):
        return 'None'
    else:
        return round(a[0]/a[2],2)
num([10, "/", 3])


# In[6]:


#The Fibonacci Number
def fibonacci():
    a, b = 1, 1
    c=[]
    while a<255:
        c.append(a)
        a, b = b, a+b
    return c
print(fibonacci())


# In[32]:


#Positive Dominant
def num(a):
    b=len(set([i for i in a if i>0]))
    c=len(set([i for i in a if i<0]))
    return b>c
num([5, 0])


# In[229]:


#Return the Objects Keys and Values
def num(a):
    b=list(a.values())
    c=list(a.keys())
    return [c,b]
num({ "key1": True, "key2": False, "key3": True} )


# In[230]:


#Next Happy Year
def num(a):
    b=list(range(a,a+50))
    c=[list(dict.fromkeys(list(str(i)))) for i in b ] 
    d=[i for i in c if len(i)==4]
    e=[int(''.join(i)) for i in d]
    if e[0]==a:
        return e[1]
    else:
        return e[0]
num(2060)


# In[233]:


#Divisible by Left Digit?
def num(a):
    b=list(str(a))
    c=[int(i) for i in b]
    d=[True if ((c[i+1])%(c[i]))==0 else False for i in range(len(c)-1)]
    return [False]+d
num(733126446456)


# In[473]:


#Birthday Cake
def num(a,b):
    c=len(a)
    if b%2==0:
        e=(c+26)*'#'
        f="# "+str(b)+" Happy Birthday "+a+"! "+str(b)+' #'
        return [e,f,e]
    else:
        g="* "+str(b)+" Happy Birthday "+a+"! "+str(b)+' *'
        k=(c+26)*"*"
        return [k,g,k]
num("Isabelle", 2)


# In[474]:


#Is the Phone Number Formatted Correctly?
def num(a):
    b=a.split('-')
    c=len(b[-1])
    d=len(b[0])
    if c==4 and d==9 and a[0]=="(" and a[4]==")":
        return True
    else:
        return False
num("(119) 555-2345")


# In[475]:


#Find the True Equations
def num(a):
    b=[i.replace('=','==') for i in a]
    d=[i if eval(i)==True else 0 for i in b]
    e=[i for i in d if i!=0]
    f=[i.replace('==','=') for i in e]
    if len(e)==0:
        return []
    else:
        return f
num(["1+1=2", "2+2=3", "5*5=10", "3/3=10"])


# In[478]:


#The Most Brilliant Exciting Fantastic Number
def num(a):
    c='The most brilliant'
    if a%2==0:
        c+=' exciting'
    if a%3==0:
        c+=' fantastic'
    if a%4==0:
        c+=' virtuous'
    if a%5==0:
        c+=' heart-warming'
    if a%6==0:
        c+=' tear-jerking'
    if a%7==0:
        c+=" beautiful"
    if a%8==0:
        c+= " exhilarating"
    if a%9==0:
        c+=" emotional"
    if a%10==0:
        c+=" inspiring"
    return c+" number is "+str(a)+'!'
        
num(21)


# In[479]:


#Count How Many Times an Element is Repeated
def num(a):
    b=list(set(a))
    c=[a.count(i) for i in b]
    d=dict(zip(b,c))
    return d
num([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0])


# In[480]:


#Fruit Salad 
def num(a):
    c=[i[0:(len(i))//2] for i in a]
    d=[i[(len(i))//2:] for i in a]
    e=[(i,j) for i,j in zip(c,d)]
    f=sorted(sum(e,()))
    return ''.join(f)
num(["banana"])


# In[481]:


#Shopping for Memorial Day!
def num(a):
    b=[d for d in a if d.get('taxable') == True]
    c=[d for d in a if d.get('taxable') == False]
    e=[(i['prc']) for i in b if 'prc' in i]
    f=[(i['qty']) for i in b if 'qty' in i]
    g=[(i['prc']) for i in c if 'prc' in i]
    h=[(i['qty']) for i in c if 'qty' in i]
    k=[(i*j) for i,j in zip(e,f)]
    m=[(i*(6/100)+i) for i in k]
    l=[(i*j) for i,j in zip(g,h)]
    n=sum(m+l)
    return n
num([
  { "desc": "potato chips", "prc": 2, "qty": 2, "taxable": False },
  { "desc": "soda", "prc": 3, "qty": 2, "taxable": False },
  { "desc": "paper plates", "prc": 5, "qty": 1, "taxable": True }
])


# In[482]:


#Regex Series: Even Number?
import re
def num(a):
    b=int(a)
    if b%2==0:
        return True
    else:
        return False
num("5578")


# In[483]:


#Club Entry
def num(a):
    b=[i for i in a if a.count(i)>1]
    c=[ord(i[0])-96 for i in b]
    d=c[0]*4
    return d
num("hill")


# In[538]:


#A Simple Check
def num(a,b):
    c=min(a,b)
    d=list(range(1,a+1))[::-1]
    e=list(range(1,b+1))[::-1]
    if c==a:
        f=[i%j==0 for i,j in zip(e,d)]
        g=[i for i in f if i==True]
        return len(g)
    else:
        h=[i%j==0 for i,j in zip(d,e)]
        k=[i for i in h if i==True]
        return len(k)
        
num(54, 27)
    


# In[539]:


#RNA Reverse Complement
def num(a):
    myDict = {'A':'U','C':'G','G':'C','U':'A'}
    lst = []
    for c in a:
        lst.insert(0, myDict[c])
    return ''.join(lst)
num("GUGU")


# In[540]:


#Random Number Generator
import random
def num():
    return int(''.join(random.sample('12345',5)))
print(num())


# In[541]:


#Random Number Generator
import random
def num():
    digits = ['1', '2', '3', '4', '5']
    random.shuffle(digits)
    return int(''.join(digits))
print(num())


# In[542]:


#Switching Between Pencils
def num(a):
    if len(a)==1:
        return 2
    else:
        b=[a[i]==a[i+1] for i in range(len(a)-1)]
        c=len(a)
        d=len([i for i in b if i==False])
        return d+c*2
num(["Blue", "Blue", "Blue", "Red", "Red", "Red"])


# In[543]:


#Ping Pong!
def num(a,b):
    c=len(a)
    if b==True:
        f=["Pong!"]*c
        d=[[i,j] for i,j in zip(a,f)]
        e=sum(d,[])
        return e
    else:
        h=["Pong!"]*(c)
        i=[[i,j] for i,j in zip(a,h)]
        j=sum(i,[])
        k=j[0:-1]
        return k
num(["Ping!", "Ping!", "Ping!"], True)


# In[1]:


#Come Check Out This Crazy Function
def num(a,b):
    return a^b
num(10,20)


# In[22]:


#Do All Bigrams Exist?
def num(a,b):
    c=''.join(b)
    d=list(set([True if i in c else False for i in a]))
    if d==[True]:
        return True
    else:
        return False
num(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"])


# In[77]:


#Delete Occurrences of Extra Elements in a List
def num(a,b):
    c=list(dict.fromkeys(a))
    return c*b
num([True, True, True], 3)


# In[78]:


#Initialize
def num(a):
    b=[i.split(' ') for i in a]
    c=sum(b,[])
    d=[i[0] for i in c]
    e=d[0::2]
    f=d[1::2]
    g=[i+j for i,j in zip(e,f)]
    h=['.'.join(i) for i in g]
    k=[i+'.' for i in h]

    return k
num(["Harry Potter", "Ron Weasley"])


# In[31]:


#Simple Numbers
def num(a,b):
    d=list(range(a,b+1))
    e=[str(i) for i in d]
    f=[list(i) for i in e]
    h=[[int(i) for i in sublist] for sublist in f]
    k=[[num ** (index + 1) for index, num in enumerate(sublist)] for sublist in h]
    m = [sum(i) for i in k]
    n=[i if i==j else False for i,j in zip(d,m) ]
    s=[i for i in n if i!=False]
    return s  
num(90, 100)


# In[45]:


#Bound Sort
def num(a,b):
    c=sorted(a[0:b[1]+1])
    d=a[b[1]+1:]
    e=c+d
    f=sorted(a)
    return e==f
num([1, 6, 5, 3, 8, 9], [0, 2])
    


# In[84]:


#Letter Distance
def num(a,b):
    if len(a)==len(b):
        c=list(a)
        d=list(b)
        e=[ord(i) for i in c]
        f=[ord(i) for i in d]
        g=sum([abs(i-j) for i,j in zip(e,f)])
        return g
    elif(len(a)>len(b)):
        aa=len(b)
        bb=a[0:aa]
        cc=a[aa:]
        dd=[ord(i) for i in bb]
        ee=[ord(i) for i in b]
        ff=sum([abs(i-j) for i,j in zip(dd,ee)])
        gg=len(a)-len(b)
        return ff+gg
    else:
        aaa=len(a)
        bbb=b[0:aaa]
        ccc=b[aaa:]
        ddd=[ord(i) for i in bbb]
        eee=[ord(i) for i in a]
        fff=sum([abs(i-j) for i,j in zip(ddd,eee)])
        ggg=len(b)-len(a)
        return fff+ggg
        
        
    
        
num("abcde", "bcdef")


# In[118]:


#Emptying the Values
def num(a):
    b=[0 if type(i)==int else 0.0 if type(i)==float else "" if type(i)==str else True if i==False else False if i==True else [] if type(i)==list else () if type(i)==tuple else set() if type(i)==set 
       else set() if i=={} else None for i in a]
    return b
num([1, 2, 3])


# In[113]:


#Spelling Bee
def num(a):
    b=a.split('.')
    c=b[0:-1]
    d=list(b[-1])
    e=''.join(d[1:-1])
    f="".join(b[0:-1])
    g=f.replace(' ','')
    h=g.lower()
    k=e.lower()
    return h==k
num("H. A. N. K. E. R. C. H. E. I. F. Handkerchief.")


# In[114]:


#Drink Sorting
from operator import itemgetter
def num(a):
    b=sorted(a, key=itemgetter('price'))
    return b
num([
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}
])


# In[115]:


#Longest Daily Streak
def num(a):
    if True in a:
        b=a.index(False)
        c=len(a[:b])
        return c
    else:
        return 0
    
num([True, True, True, False, True, True])


# In[120]:


#Sock Pairs
def num(a):
    b=list(a)
    c=len([i for i in b if b.count(i)%2==0])/2
    return c
num("CABBC")


# In[160]:


#Dashed Vowels
def num(a):
    b=a.replace('a','-a-')
    c=b.replace('e','-e-')
    d=c.replace('i','-i-')
    e=d.replace('o','-o-')
    f=e.replace('u','-u-')
    g=f.replace('A','-A-')
    h=g.replace('E','-E-')
    i=h.replace('I','-I-')
    j=i.replace('O','-O-')
    k=i.replace('U','-U-')
    return k  
num("Fight for your right to party!")


# In[20]:


#Find the Missing Letter
def num(a):
    b=[ord(i) for i in a]
    c=list(range(b[0],b[-1]+1))
    d=[chr(i) for i in c]
    e=[i for i in d if i not in a]
    return e[0]
num(["a", "b", "c", "e", "f", "g"])


# In[21]:


#Sort By Index of Character
from operator import itemgetter
def num(a,b):
    c=sorted(a, key=itemgetter(b-1))
    return c
num(["az16", "by35", "cx24"], 2)


# In[22]:


#Negative Image
def num(a):
    b=[len(i) for i in a]
    c=sum(a,[])
    d=[0 if i==1 else 1 for i in c]
    e=[d[i:i+b[0]] for i in range(0, len(d), b[0])]
    return e
num([
  [1, 1, 1],
  [0, 0, 0]
])


# In[23]:


#Count the Smiley Faces :)
def num(a):
    b=[':-)',":~)",";-)",';~)',";~D",":-D",":~D",":)",":D",";)",";D",';-D']
    c=len([i for i in a if i in b])
    if c==[]:
        return 0
    else:
        return c
num([";D", ":-(", ":-)", ";~)"])


# In[24]:


#Is It the Same Upside Down?
def num(a):
    b=list(a)
    c=''.join([i.replace('6','9') if i=='6' else i.replace('9','6') if i=='9' else '0' for i in b])
    return c[::-1]==a
num("6090609")


# In[65]:


#Sum of Two Numbers in List Equal to Given Number
def num(a,b):
    d=[i+j==b for i,j in zip(a,a[1:])]
    return d
num([2, 8, 9, 12, 45, 78], 1)


# In[37]:


#Concatenate to Form Target List
def num(a,b):
    c=sum(a,[])
    return sorted(b)==sorted(c)
num([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7])


# In[52]:


#Average Word Length
def num(a):
    b=a.split(' ')
    c=len(b)
    d=a.lower()
    e=''.join([i for i in d if i in 'abcdefghijklmnopqrstuvwxyz'])
    f=len(e)/c
    return round(f,2)
num("Dude, this is so awesome!")


# In[57]:


#Minimum Difference Pair
def num(a):
    b=sorted(a)
    c=[(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a))]
    return c
num([40, 16, 8, 17, 15])


# In[66]:


#Minimum Difference Pair
def num(nums):
    a= sorted(nums)
    b = [a[i]-a[i-1] for i in range(1,len(a))]
    c = b.index(min(b))
    return a[c:c+2]
num([40, 16, 8, 17, 15])


# In[72]:


#Minimum Difference Pair
def num(a):
    b=sorted(a)
    c=min(abs(i-j) for i,j in zip(a,a[1:]))
    d= ([[i,j] for i,j in zip(a,a[1:]) if abs(i-j)==c])
    e=min(d)
    return e
num([1, -31, -27, -18, -48, -15, -11, -34])


# In[129]:


#Consecutive Numbers
def num(a,b,c):
    d=sorted(a)
    e=[i for i in range(len(a)) if a[i]==b]
    f=[abs(i-j) for i,j in zip(e,e[1:])]
    if b not in a and c==0:
        return True
    elif len(a)<c:
        return False
    elif b in a and c==0:
        return False
    elif b in a and a.count(b)==1 and c==1:
        return True
    elif b in a:
        k=sum([i for i in f if i==1])+1
        return k==c
    else:
        return False
        
num([5, 5, 5, 5, 5], 5, 5)    


# In[149]:


#Consecutive Numbers
def num(a,b,c):
    d="".join([str(i) for i in a])
    e=str(b)*c
    if e in d:
        return True
    else:
        return False
num([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2)


# In[200]:


#A Possible Shape?
def num(a,b):
    if a<3:
        return False
    elif len(b)!=a:
        return False
    elif len(b)==a:
        c=[i for i in b if i>180]
        return len(c)==0
    else:
        return True
num(1, [21])
    


# In[201]:


#Converting One Binary String to Another
def num(a,b):
    c=[i==j for i,j in zip(a,b)]
    d=len([i for i in c if i==False])
    return d/2
num("10011001", "01100110")


# In[202]:


#Word to Bitstring to Boolean List
def num(a):
    b=list(a)
    c=[ord(i)-96 for i in b]
    d=[i-1 for i in c]
    e=[False if i%2!=0 else True for i in d]
    return e
num('tesh')


# In[215]:


#Word Builder
def num(a,b):
    d=[[i,j] for i,j in zip(a,b)]
    e=sorted(d, key=lambda x: x[1])
    f=sum(e,[])
    g=''.join([str(i) for i in f if str(i) in 'abcdefghijklmnopqrstuvwxyz'])
    return g
num(["g", "e", "o"], [1, 0, 2])


# In[216]:


#Fractions and Rounding
def num(a,b):
    c=round(eval(a),b)
    d=a+" "+"rounded to"+" "+str(b)+" decimal places is "+str(c)
    return d
num("22/7", 2)
    


# In[222]:


#Just Another Sum Problem But... 
def num(a,b):
    c=min(a,b)
    d=max(a,b)
    e=[c,d]
    f=sum(list(range(c,d+1)))
    return f
num(-20, 5)


# In[235]:


#Trailing Zeros
def num(a):
    b=0
    while(a>=5):
        a//=5
        b+=a
    return b
        
num(1000)


# In[263]:


#Unfair Hurdles
def num(a):
    b=len(a)
    c=a[0]
    d=[i for i in a[0] if i==' ' ]
    f=len([i for i in a[0] if i=='#'])-1
    e=len(d)
    k=e/f
    if b>=4:
        return True
    elif k<4:
        return True
    else:
        return False
num([
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #",
  "#    #    #    #"
])


# In[266]:


#Christmas Tree
def num(a):
    b=list(range(1,a+1))
    
    return b
num(5)


# In[274]:


#Function Factory
def num(a): 
    c=lambda x:x+a
    print(c(10))
num(5)


# In[302]:


#Convert "Zero" and "One" to "1" and "0"
def num(a):
    b=a.lower()
    c=b.split(' ')
    d=''.join(['0' if i=='zero' else '1' if i=='one' else '' for i in c])
    if len(d)<8:
        return ''
    elif len(c)%8==0:
        return d
    else:
        e=(len(d)//8)*8
        f=d[:e]
        return e
num("one one")


# In[322]:


#Keeping Count
def num(a):
    b=list(str(a))
    c=[b.count(i) for i in b]
    d=int("".join([str(i) for i in c]))
    return d
num(2)


# In[336]:


#Replacing Letters with Hashes
def num(a,b):
    d=b.split("-")
    e=[ord(i) for i in d]
    f=list(range(e[0],e[-1]+1))
    g=[chr(i) for i in f]
    c="".join(['#' if i in g else i for i in a])
    return c
num("", "a-z")


# In[353]:


#Divide a Fraction by Two
from fractions import Fraction
def num(a):
    b=str(eval(a)*(1/2))
    print (Fraction(str(b)))
num("3/8")


# In[371]:


#List Chunking
def num(a,b):
    c=[a[i:i+b] for i in range(0, len(a), b)]
    return c
num([1, 2, 3, 4], 2)


# In[64]:


#Number of Even or Odd Digits
def num(a,b):
    c=[list(str(i)) for i in a]
    d=[[int(i) for i in substring] for substring in c]
    if b=='odd':
        e=[[i for i in sub if i%2!=0] for sub in d]
        g=[len(i) for i in e]
        return g
    else:
        f=[[i for i in su if i%2==0] for su in d]
        h=[len(i) for i in f]
        return h
num([54, 113, 89, 10], "even")


# In[390]:


#Changing a String into camelCase
def num(a):
    b=[i for i in a if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    return b
num("snake_case")


# In[399]:


#Sum of the Items in a List
def num(a):
    b=sum(i if isinstance(i, int) else num(i) for i in a)
    return b
num([1, 2, 3])


# In[421]:


#Recursion: Palindrome Word
def num(a):
    b=a[::-1]
    return b==a
num("rotor")


# In[442]:


#Truncate String at a Given Length
def num(a,b):
    c=a[0:b]
    d=a.split(" ")
    e=c.split(' ')
    f=" ".join([i for i in e if i in d])
    return f
num("Lorem ipsum dolor sit amet.", 17)


# In[443]:


#Changing a String into camelCase
def num(a):
    b=a.replace("_",' ')
    c=b.split(' ')
    d=[i.title() for i in c[1:]]
    e="".join([c[0].lower()]+d)
    
    return e
num("low high_HIGH")


# In[444]:


#Sum of the Items in a List
def num(a):
    b=sum(i if isinstance(i, int) else num(i) for i in a)
    return b
num([1, 2, 3])


# In[31]:


#Find First Character That Repeats
def num(a):
    b=''.join(list(dict.fromkeys(a)))
    if a==b:
        return -1
    else:
        c=[i for i in a if a.count(i)>1]
        return c[0]
num("legolas")


# In[37]:


#Merge Two Lists
def num(a,b):
    if len(a)==len(b):
        c=[[i,j] for i,j in zip(a,b[0:len(a)+1])]
        d=sum(c,[])
        return d
    elif len(a)<len(b):
        e=b[0:len(a)]
        f=b[len(a):]
        g=[[i,j] for i,j in zip(a,e)]
        h=sum(g,[])+f
        return h
    else:
        ee=b[0:len(b)]
        ff=b[len(b):]
        gg=[[i,j] for i,j in zip(a,ee)]
        hh=sum(gg,[])+ff
        return hh
        
        
num(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])


# In[38]:


#Generating and Swapping Key-Value-Pairs in Dictionary
def num(a,b,c):
    if c==False:
        return dict(zip(a,b))
    elif c==True:
        return dict(zip(b,a))
    else:
        return {}
num(["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True)


# In[74]:


#Numbers in Strings
def num(a):
    b=[i for i in a if any(char.isdigit() for char in i)]
    return b
num(["abc", "abc10"])


# In[81]:


#Pages in a Book
def num(b):
    return ((8 * b) + 1)**.5 % 1 == 0
num(9453)


# In[98]:


#Smallest N Digit Number
def num(a,b):
    c=int(str(1)+str(0)*(a-1))
    d=list(range(c,c+101))
    e=min([i for i in d if i%b==0])
    return e
num(2, 3)
    


# In[137]:


#Find the Largest Prime within a Range
import sympy
def num(a,b):
    c=min(a,b)
    d=max(a,b)
    e=list(range(c,d+1))
    f=max([i for i in e if sympy.isprime(i)])
    return f
num(2,10)


# In[31]:


#Hamming Code
def num(a):
    b=list(a)
    c=[ord(i) for i in b]
    d=[bin(i) for i in c]
    e="".join([i.replace('b','')*3 for i in d])
    return e
num('matt')


# In[32]:


#White Spaces Between Lower and Uppercase Letters
def num(a):
    c="".join([i.replace(i,' '+i) if i.isupper() else i for i in a])
    d=c[0:2]
    e=[i for i in d if i.isupper()]
    f=e[0]+c[2:]
    return f
num("TheGreatestUpsetInHistory")


# In[37]:


#The Major Sum
def num(a):
    b=sum([i for i in a if i>0])
    c=sum([i for i in a if i<0])
    d=[str(i) for i in a]
    e=len([i for i in d if i.count('0')])
    if b>(-1*c) and b>e:
        return b
    elif c*(-1)>b and (c*-1)>e:
        return c
    else:
        return e
num([0, 0, 0, 0, 0, 1, 2, -3])


# In[55]:


#Diamond Shaped Array
def num(a):
    b=list(range(1,a+1))
    c=[str(i) for i in b]
    d=[[i]*j for i,j in zip(c,b)]
    e=[[int(i) for i in sublist] for sublist in d]
    f=e[::-1][1:]
    g=e+f
    return g
num(5)


# In[80]:


#One Plus One
def num(a):
    b=a.lower()
    c=b.replace('one','1')
    d=c.replace('zero','0')
    e=d.replace('two','2')
    f=e.replace('plus','+')
    g=f.replace('minus','-')
    if eval(g)==0:
        return 'Zero'
    elif(eval(g)==1):
        return 'One'
    elif(eval(g)==2):
        return 'Two'
    elif(eval(g)==3):
        return 'Three'
    elif eval(g)==4:
        return 'Four'
    elif eval(g)==-1:
        return 'minus One'
    else:
        return 'minus Two'

num("one minus two")


# In[110]:


#Word Riddles
def num(a):
    b=a.lower()
    c=b.split('in')
    d=c[1]
    e=d[1:]
    f=c[0]
    g=d[0]
    h=g+f+e
    i=h.upper()
    return i
num("Finland")


# In[30]:


#Minimum Removals to Make Two Strings Anagrams
def num(a,b):
    c=len([i for i in a if i not in b])
    d=len([i for i in b if i not in a])
    return c+d
num("acb", "ghi")
    


# In[31]:


#Indicate the Media Type from HTTP Response Header
import requests
def content_type(url):
    return requests.get(url).headers["content-type"]


# In[33]:


#Hall Monitor
def num(a):
    b=a[0::2]
    c=list(set(a[1::2]))
    d=a[1::2]
    e=list(set(a[0::2]))
    f=a[1::2]
    g=a[0::2]
    if len(b)==len(d) and c==['H']:
        return True
    elif len(b)==len(d)+1 and c==['H']:
        return True
    elif len(f)+1==len(g) and e==['H']:
        return True
    elif len(g)==len(f) and e==['H']:
        return True
    else:
        return False
num([1, 2, "H", 3])


# In[52]:


#Convert String to camelCase
def num(a):
    if '-' in a:
        b=a.split('-')
        c=b[1:]
        d=[b[0]]
        e=[i.title() for i in c]
        f=d+e
        g=''.join(f)
        return g
    else:
        bb=a.split('_')
        cc=bb[1:]
        dd=[bb[0]]
        ee=[i.title() for i in cc]
        ff=dd+ee
        gg=''.join(ff)
        return gg
        
num("The_Stealth_Warrior")


# In[47]:


#Most Common Last Vowel
def num(a):
    b=a.split(' ')
    c=[i[-1] for i in b ]
    d=[i for i in c if i in 'aeiouAEIOU']
    e=d[-1].lower()
    return e
    
num("OOI UUI EEI AAI")


# In[48]:


#Strictly Increasing or Decreasing
def num(a):
    b=sorted(list(set(a)))
    c=b[::-1]
    if a==b:
        return 'increasing '
    elif a==c:
        return 'decreasing'
    else:
        return 'neither'
num([3, 2, 1])


# In[49]:


#The List Twins
def num(a):
    for i in range(len(a)):
        if sum(a[:i])==sum(a[i:]):
            return i
num([10, 20, 30, 5, 40, 50, 40, 15])


# In[50]:


#Digits Sum Root
def root_digit(n):
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n
root_digit(8)


# In[51]:


import sympy
def num(a):
    c=1
    b=list(sympy.primerange(2,sympy.prime(a+1)))
    for i in b:
        c=c*i
    return c
num(1)


# In[52]:


#Any Prime Number in Range
import sympy
def num(a,b):
    c=list(range(a,b+1))
    d=[i for i in c if sympy.isprime(i)]
    if len(d)>=1:
        return True
    else:
        return False
num(3, 5)


# In[108]:


#Names, Ages and Occupations
def num(a):
    b=a.split(',')
    c=['name','age','occupation']
    d=dict(zip(c,b))
    if a=='':
        return {}
    else:
        return d
num("John Mayer, 41, Singer")


# In[110]:


#Domino Chain
def domino_chain(dominos):
    dominos = list(dominos)
    for i, d in enumerate(dominos):
        if d in [' ', '/']:
            break
            dominos[i] = '/'
        return ''.join(dominos)
domino_chain('/// ||')


# In[120]:


#Convert camelCase to snake_case
def num(a):
    b=[i.replace(i,"_"+i) if i.isupper() else i for i in a]
    c="".join(b).lower()
    return c
num("thatsGreat")


# In[131]:


#camelCase ⇄ snake_case
def num(a):
    if "_" in a:
        b=a.split("_")
        c=[i.capitalize() for i in b[1:]]
        d=[b[0]]+c
        e=''.join(d)
        return e
    else:
        f=[i.replace(i,"_"+i) if i.isupper() else i for i in a]
        g="".join(f).lower()
        return g
        
num("getColor")
    


# In[177]:


#Wiggled Strings
def num(a):
    b=len(a)
    c=list(range(1,len(a)+1))
    d=[i*' ' for i in c]
    e=[i+a for i in d]
    f=e[::-1]
    return e+f
num("hello")


# In[267]:


#Spicy Food
def num(a,b):
    c=[[i,j] for i,j in zip(a,b)]
    d=[[str(i) for i in sublist] for sublist in c ]
    e=[i for i in d if i[0] == 'S']
    f=[i for i in d if i[0]=='N']
    g=sum(e,[])
    k=[i for i in g if i!='S']
    m=sum([int(i) for i in k])
    h=sum(f,[])
    l=[i for i in h if i!='N']
    n=sum([int(i)/2 for i in l])
    return [m+n,n]
num(["S", "N"], [41, 10])


# In[270]:


#Greater Than the Sum?
def num(a):
    b=[sum(a[:i])<j for i,j in enumerate(a)]
    return all(b)
num([1, 2, 4, 6, 13])


# In[271]:


##Greater Than the Sum?
def num(a):
    b=0
    for i in a:
        if i<=b:
            return False
        b=b+i
    return True
num([1, 2, 4, 6, 13])


# In[272]:


#Back and Forth
def num(a):
    b=''.join(a)
    c=sum([i.count('>') for i in b])
    d=sum([i.count("<") for i in b])
    if c>d:
        e=(c-d)*'>'
        return e
    else:
        f=(d-c)*'<'
        return f
num([">>>", "<<<"])


# In[273]:


#Longest Word in a 7 Segment Display
def num(a):
    b=[i for i in a if len(i)>=7]
    c=[i for i in b if all(c not in 'kmvwx' for c in i)]
    return c
num(["velocity", "mackerel", "woven", "kingsmen"])


# In[274]:


#Remix the String
from operator import itemgetter
def num(a,b):
    c=list(a)
    d=[[i,j] for i,j in zip(b,c)]
    e=sorted(d,key=itemgetter(0))
    f=sum(e,[])
    g=[str(i) for i in f]
    h=[i for i in g if i not in '0123456789']
    return ''.join(h)
num("computer", [0, 2, 1, 5, 3, 6, 7, 4])


# In[7]:


#Sort a String by Its Last Character
from operator import itemgetter
def num(a):
    b=a.split(' ')
    d=sorted(b,key=itemgetter(-1))
    e=' '.join(d)
    return e
num("sample partner autonomy swallow trend")


# In[15]:


#A Pirate's Tale
def num(a):
    b=sum([abs(i) for i in a])
    if b%5==0:
        c=b/5
        d=b+c-1
        return d
    else:
        e=b//5
        f=b+e
        return f
num([-1, -2])    


# In[37]:


#Total Sales of Product
def num(a,b):
    c=sum(a,[])
    if b in c:
        d=len(a)
        e=len(c)
        f=int(e/d)
        g=c.index(b)
        h=c[g::f]
        k=[str(i) for i in h]
        l=[i for i in k if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
        m=sum([int(i) for i in l])
        return m
    else:
        return "Product not found"
    
        
num([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "D")


# In[8]:


#Expand a Number I
def num(a):
    b=list(str(a))
    c=[i for i in enumerate(b) if i!=0]
    return c
num(70304)


# In[25]:


#Global Variable
x=-1

def counter():
    global x
    x += 1
    return x
print(counter())


# In[1]:


#Swimming Pool
def num(a):
    b=a[0]
    c=a[-1]
    d=b+c
    e=[i for i in d if i ==1]
    if len(e)>=1:
        return False
    else:
        return True
num([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0]
])


# In[2]:


#Making Change
def num(a):
    if len(a) == 1:
        return a[0]
    else:
        b = [a[i + 1] - a[i] for i in range(len(a) - 1)]
        return num(b)

result = num([5, 8, 8])
print(result)


# In[43]:


#Triple Letter Groupings
def num(a):
    b=[a[i:i+3] for i in range(0, len(a), 1)]
    c=sorted([i for i in b if len(i)==3])
    return c
num("hi")


# In[45]:


#Order by Length First
from operator import itemgetter
def num(a):
    lengths = set(map(len, a))
    c=[[i for i in a if len(i)==sublist] for sublist in lengths]
    d=len(c)
    if (d==1):
        e=sum(c,[])
        return sorted(e)
    else:
        f=[sorted([(i) for i in sub]) for sub in c]
        g=sum(f,[])
        return g
num(["this", "is", "a", "small", "test"])


# In[58]:


#order by Length First
def num(a):
    b=sorted(sorted(a),key=len)
    return b
num(["cat", "ran", "for", "the", "rat"])


# In[59]:


#Hidden Calculator Words
def num(a):
    dic = {'1':'I', '2':'Z', '3':'E', '4':'H', '5':'S', '6':'G', '7':'L', '8':'B', '9':'', '0':'O', '.':''}
    return ''.join([dic[i] for i in str(a)[::-1]])
num(3045) 


# In[75]:


#Making Change
import sympy
def num(a):
    b=list(range(1,a+1))
    c=[i for i in b if sympy.isprime(i)]
    return c
num(20)
    


# In[83]:


#Summation of the First n Terms
def summation(exp, i):
    total = 0
    for n in range(1, i + 1):
        total += eval(exp.replace("n", str(n)))
    return total

# Test cases
print(summation("n", 10))    # Output: 55
print(summation("1/n", 50))  # Output: 4.5
print(summation("n**n", 6))  # Output: 50069


# In[84]:


def summation(exp, i):
    b=round(sum(eval(exp) for n in range(1,i+1)),1)
    return b
summation("n", 10)


# In[ ]:


#Gold Distribution
def num(a):
    b=[]
    c=[]
    while(len(a)>0):
        if 

