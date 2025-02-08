n=int(input("enter how many number"))
list1=[]
list2=[]
#input from users create list1
for i in range(n):
    list1.append(int(input("enter data")))
print(list1)
list1.sort(reverse=True)
print(f"sorting list1 {list1}")
#store unic value in new list(list2)
for value in list1:
    if value not in list2:
        list2.append(value)
print("print list2")
print(list2)
#print nth nuber of maximum number
no=int(input("enter numbers of maximum you need"))
print(f"{no} max is {list2[no-1]}")
##index=0
###start logic here 
##if no<=len(list2):
##    for i in range(no):
##        s=list1.count(list1[index])
##        index+=s
##    print(f"{no}-- max number is{list1[index-1]}")
##else:
##    print(f"{no}max is not avl in this list" )

