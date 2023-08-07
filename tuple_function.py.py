t1=(1,2,3,4,2)
print("\ntuple - ",t1)
print(t1[0])

#duplicate tuple
t1=t1*3
print("\nduplicate tuple -\n",t1)

#count function
c=t1.count(2)
print("\n2 is repeat in ",c," times")

#search function
i=t1.index(4)
print("\n4 search in ",i,"times")

#delete tuple
del(t1)
