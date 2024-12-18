
my_list_1=["c","c++","python","java","java-script"]
my_stack=[]
for i in range(len(my_list_1)):
   my_stack.append(my_list_1[i])
print(my_stack)
print()

# poping the data from the my_stack list
my_list_2=[]
for i in range(len(my_stack)):
   pop_data=my_stack.pop()
   my_list_2.append(pop_data)
   print(my_list_2)
print()

# updating the data in my_list

my_list=["pavan","akhil","srinivas","ramana","ravindar","venkant"]

def update_data(new_data,change_data):
    for i in range(len(my_list)):
       if my_list[i]==change_data:
          my_list[i]=new_data
    return my_list

print(update_data("srinu","pavan"))



