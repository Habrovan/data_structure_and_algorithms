def sum_even_numbers(my_list):
    sum = 0
    for m in my_list:
        if m%2==0:
          sum=sum+m
    return sum 

my_list=[]
z=int(input("Enter number of Elements: "))
for i in range (1,z+1):
   y=int(input("Enter Interger in a List: "))
   my_list.append(y)

print(sum_even_numbers(my_list))