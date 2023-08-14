import array as arr
a=arr.array('i',[1,2,3])
print("New Array")
for i in range(0,3):
    print(a[i],end=" ")
a1=arr.array('d',[2.5,1.5,3.5])
print("\n\nfloat array")
for i in range(0,3):
    print(a1[i],end=" ")

print("\ninsert array element-")
a.insert(1,4)
print(a)

print("\ninsert at end-")
a.append(5)
#print(a)

for i in range(0,5):
    print(a[i],end=" ")

print("\n\nafter removing 2 and pop last elment-")   
a.remove(2)
a.pop()
for i in range(len(a)):
    print(a[i],end=" ")

#print(a[2])
