print('Welcome to python ',end='')  #Concatenate with the next line
print("Programming ")
#Using separator variable
print('Today is',end=' ')
print(17,6,2023,sep='/')

#Variables
Num=17
print(Num)
print(type(Num))

name="Joyce"
print(name)
print(type(name))

a=1.23
print(a)
print(type(a))

b=12.457889
print(b)
print(type(b))
#Get input from user
input("Enter your name:")
#Get input from user and output on the screen
print(input("Enter your name:"))
#store user input on a vaiable
firstname=(input("Enter your first name:"))
print(firstname)
#Adding numbers
num_1=input("Enter the first number")
num_2=input("Enter the second number")
sum=int(num_1)+int(num_2)
print(sum)
#List
text=[12,"abc",45,"abc"]
print(text)
print(type(text))
#tuple
text_1=(12,"abc",45,"abc")
print(text_1)
print(type(text_1))

#set
text_2={12,"abc",45,"abc"}
print(text_2)
print(type(text_2))

text_3={
    "Name":"Wamboi",
    "Age":45,
    "salary":20000
}
print(text_3)
print(type(text_3))