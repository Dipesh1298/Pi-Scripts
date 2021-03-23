print('Hello world')
a=5
b=6
c=a+b
a=c-a
b=c-a
print(a)
print(b)
a=0.1
b=0.2
c=0.3
print(a+b-c)
print(type(a+b-c))
mystring= 'abcdefghijk'
print(mystring[2:4])
print(mystring[:4])
print(mystring[4:])
print(mystring[::2])
x=" dipesh deepu Kushwaha"
x=x.upper()
print(x)
x=x.split()
print(x)
print("this is a {}".format("laptop"))
print("this is a {f}".format(f="laptop"))
print("this is a {}".format("car"))
print("this is a {l} price is{p}".format(l="laptop",p=' 50000'))
print(set('mississippi'))
print(1==2)
myfile=open('myfile.txt',mode='w')
myfile.write('forth line\none \n two\n three')
myfile.close()
myfile=open('myfile.txt')
loc='abc'
if loc=="Loc":
    print(myfile.read())
elif loc=="squreroot":
    print(100**0.5)
else:
    print(5==8)

   
mylist=[1,2,3,4,5,7,9,46]
listsum=0
for num in mylist:
 if num%2==0:
    txt2 = "even number :{a}".format(a=num) 
    print(txt2)
    listsum=listsum+num
    
 else:
    txt2 = "Odd number :{b}".format(b=num) 
    print(txt2)
print("sum of even number:")
print(listsum)    
x = 0
while x < 5:
    txt = " the currnet value of x is:{y}".format(y = x)
    print(txt)
    x =x + 1
index_count = 0
word = 'abc'
for letter in word:
    print(word[index_count])
    index_count +=1
for item in enumerate(word):
    print(item)
print(list(range(0,15,2)))
print([x for x in range(1,51) if x%3 == 0])
mylist.append(6)
print(mylist)
mylist.pop()
print(mylist)
#help(mylist.insert)
def py_abn():
    print("hello")
py_abn()
def add_num(num1, num2):
    return num1+num2
result= add_num(12,56) 
print(result)  
def say_hello(name):
    print('Hello'+ name)

say_hello('Dipesh')
def even_chek(number):
    result = number%2 ==0
    print(result)
even_chek(22)
def check_even_list(mylist):
    even_number = []
    for number in mylist:
        if number %2 ==0:
           even_number.append(number)
        else:
            pass
      
    print(even_number)  

check_even_list([4,5,6,7,8,90,43,56,89])  
student_marks = [('ram',65),('tom',199),('mama',96)]
def student_check(student_marks):
    current_marks = 0
    student_name = ''
    for name, marks in student_marks:
        if marks > current_marks:
            current_marks = marks
            student_name = name
        else:
           pass
    print(student_name,current_marks)
student_check(student_marks) 

def myfunc(a,b,c=0,d=0,e=0):
    result =sum((a,b,c,d,e))*0.05
    print(result)
myfunc(10,45,68,89)   

def myfunc(*args):
    result =sum((args))*0.05
    print(result)
myfunc(10,45,68,89,765,78) 

def myfun(**kwargs):
   if 'fruit' in kwargs:
       print('my fruit of choice is {}'.format(kwargs['fruit']))
   else:
        print("i did not find any fruit here")
   print(kwargs)     
myfun(fruit='apple',vegi='aalu') 
print("Ram")


      


    


   

        
       







