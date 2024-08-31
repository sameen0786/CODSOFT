def add (n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("please enter the option-\n" \
    "1. add\n"\
    "2. sub\n"\
    "3. multiply\n"\
    "4. div\n")
option=int(input("select operation from 1,2,3,4:"))
num_1=int(input("enter first number:"))
num_2=int(input("enter second number:"))
if option==1:
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif option==2:
    print(num_1,"-",num_2,"=",sub(num_1,num_2))
elif option==3:
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif option==4:
    print(num_1,"/",num_2,"=",div(num_1,num_2))
else:
    print("invalid option")
