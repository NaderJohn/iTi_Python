#Nader John
x=input("enter string ")
x=str(x)
counter=0
vowels="a,e,i,o,u,A,E,I,O,U"
for i in x:
    if i in vowels:
     counter+=1
print(counter)