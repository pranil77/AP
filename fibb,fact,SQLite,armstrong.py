Fibonacci series

def fb(n):
    
    if n<0:
        print("cccccccccccccccc")    
    elif n==0:
        return 0    
    elif n==1 or n==2:
        return 1     
    else:
        return fb(n-1) + fb(n-2)        
print(fb(3))
  

Factorial program

n=int(input("enter the no :"))
fact=1
for i in range(1,n+1):
    fact = fact * i
print("fact of givben no is :" , fact)


SQLite

connection = sqlite3.connect("users.db")
cursor = connection.cursor()
#cursor.execute("create table Student1(sno primary key,name text,class text,Address text,Email text)")
cursor.execute("insert into student1 values(1,'pranil','MCA','Mumbai','pranil123@gmail.com')")
cursor.execute("insert into student1 values(2,'rohan','MCA','Pune','rohan234@gmail.com')")
cursor.execute("insert into student1 values(3,'pranav','MBA','Nashik','pranav999@gmail.com')")
cursor.execute("insert into student1 values(4,'chetan','MCA','Nagpur','chetan777@gmail.com')")
cursor.execute("insert into student1 values(5,'Samarth','MBBS','Karachi','samarth177@gmail.com')")
result=cursor.execute("select * from student1")
for row in result:
    print("Roll No =", row[0])
    print("Name=",row[1])
    print("Class =", row[2])
    print("Address =", row[3])
    print("Email =", row[4])


armstrong number

n = int(input("Enter the number: "))
sum = 0
temp=n
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if (sum==n):
    print(("The number is an armstrong number"))
else:
    print("mca student")

