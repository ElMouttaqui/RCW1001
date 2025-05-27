mylist=[1,3,5,7,11]
i,j=0,len(mylist)-1
while(i<j):
    temp=mylist[i]
    mylist[i]=mylist[j]
    i+=1
    j-=1
    print(mylist)