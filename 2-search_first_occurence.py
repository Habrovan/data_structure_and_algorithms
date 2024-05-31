def find_first_occurence(my_list,num):
    if num in my_list:

        for k in range (len(my_list)):
            if my_list[k]==num:
               return k
    else:
       return None
    
my_list=[]
x=int(input("Enter a Number of Element: "))
for k in range (1,x +1):
    y=int(input("Enter Intergers in a list: "))
    my_list.append(y)
num=int(input("Enter a Num: "))
print(find_first_occurence(my_list,num))