##list1=[1,2,3,4,5,6]
##print(len(list1))
##lst="deepak"
##lst1=list(lst)
##print(lst1)
##lst2=lst1[::-1]
##lst3=list(range(5))
##print(lst3)
##lst4=[10,20,30,40,50]
##print(lst4[4])
##print(lst4.index(50))
##for i in range(len(lst4)):
##    print(lst4[i],end=' ')
##
##swap last and first element of list
##lst=[12,23,13,23,41,13,15,13]
##print(lst)
#(with using 3rd variable)
##temp=lst[0]
##lst[0]=lst[-1]
##lst[-1]=temp
##print(lst)
#------------------
#(with out using 3rd variable)
##lst[0]=lst[0]+lst[-1]
##lst[-1]=lst[0]-lst[-1]
##lst[0]=lst[0]-lst[-1]
##print(lst)
#------------------
##lst[0],lst[-1]=lst[-1],lst[0]
##print(lst)
#------------------
#find in list

##s=100
##if s in lst:
##    print(f'{s} present in given list ')
##else:
##    print(f'{s} not present in given list')
##-----------------
#find number in list

##s=13
##lst1=[]
##for i in range(len(lst)):
##    if lst[i]==s:
##        lst1.append(i)
##print(f"the {s} is present index is {lst1}")
##------------------
#find frequency

##cr=0
##for i in lst:
##    c=lst.count(i)
##    if c>cr:
##        cr=c
##        num=i
##print(f"find high frequency of number given string is\n{num}-{cr}")
#--------------------------
#slice operator
#-------------
##lst=[10,20,30,40,50,60,70,80,90,100]
##print(lst)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##lst1=lst[0:10:1]
##print(lst1)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##lst2=lst[::]
##print(lst2)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##lst3=lst[1:-3]
##print(lst3)#[20, 30, 40, 50, 60, 70]
##lst4=lst[::1]
##print(lst4)#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##lst5=lst[::-1]
##print(lst5)#[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
##lst6=lst[-5:5]
##print(lst6)#[]
##lst7=lst[:5:-1]
##print(lst7)#[100,90,80,70]
##lst8=lst[0::-1]
##print(lst8)#[10]
##lst9=lst[-3:3]
##print(lst9)#[]
##lst10=lst[-7:5]
##print(lst10)#[40,50]
##lst11=lst[3:-8]
##print(lst11)#[]
##for i in range(0,11)[1:5]:
##    print(i,end=" ")
##    
##print()
##for i in range(0,11)[1:5]:
##    print(lst[i],end=" ")
##print()
##for i in lst[1:5]:
##    print(i,end=' ')
###--------------------------------
###slice object
#------------
##s1=slice(3)
##lst1=lst[s1]
##print(lst1)
##s2=slice(2,9,2)
##lst2=lst[s2]
##print(lst2)

##list="123"
##list1=list[::-1]
##print(list1)
##if list==list1:
##    print("not poillindrom")
##else:
##    print("polindrom")
#----------------------

    
